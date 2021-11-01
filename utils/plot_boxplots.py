import sys
sys.path.append('/cellar/users/andreabc/scripts')
from plot_medians_in_boxplot import plot_medians_in_boxplot
from statannot import add_stat_annotation
from stat_annot_utils import create_pairs

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')
sns.set_style('ticks')

def plot_boxplots(df, x, y=None, y_list=None, order=None, ylim_dict=None, figsize=(7,4), savepath=None, suptitle=None):
	if y and y_list:
		print('ERROR. Cannot have y and y_list at the same time')
		return 

	plt.figure(figsize=figsize)
	if not order:
		order = df[x].unique()

	if y_list:

		i=1
		
		for y in y_list:
			plt.subplot(1,len(y_list),i)
			ax = sns.boxplot(x=x, y=y, data=df, order=order)

			if ylim_dict:
				if y in ylim_dict:
					plt.ylim(ylim_dict[y])

			add_stat_annotation(ax=ax, x=x, y=y, data=df, test='Mann-Whitney', text_format='simple', order=order, 
								box_pairs=create_pairs(order), verbose=0, loc='outside', comparisons_correction=None)
			plot_medians_in_boxplot(ax=ax, medians=df.groupby([x])[y].median(), 
									vertical_offset=df[y].median() * 0.05)
			counts = df[x].value_counts()
			ax.set_xticklabels(['{}\n({})'.format(x.get_text(),counts.loc[x.get_text()]) for x in ax.get_xticklabels()])
			plt.xlabel('')
			i+=1
		plt.tight_layout()

		if suptitle:
			plt.suptitle(suptitle, y=1.05)
		
	else:
		ax = sns.boxplot(x=x, y=y, data=df, order=order)

		if ylim_dict:
			if y in ylim_dict:
				plt.ylim(ylim_dict[y])

		add_stat_annotation(ax=ax, x=x, y=y, data=df, test='Mann-Whitney', text_format='simple', order=order, 
							box_pairs=create_pairs(order), verbose=0, loc='outside', comparisons_correction=None)
		plot_medians_in_boxplot(ax=ax, medians=df.groupby([x])[y].median(), 
								vertical_offset=df[y].median() * 0.05)
		counts = df[x].value_counts()
		ax.set_xticklabels(['{}\n({})'.format(x.get_text(),counts.loc[x.get_text()]) for x in ax.get_xticklabels()])
		plt.xlabel('')
	if savepath:
		print(savepath)
		plt.savefig(savepath, bbox_inches='tight')
		plt.show()
	return 