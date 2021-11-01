def plot_medians_in_boxplot(medians, vertical_offset, ax, hue_left_right=None, verbose=False, fontcolor='w', round_by=2):
    '''Adds medians to seaborn boxplot. Right now, hue only works for 2.
    example medians: df.groupby(['x_variable'])['y_variable'].median()
    example vertical_offset: df['y_variable'].median() * 0.05
    example hue_left_right: ['left_hue_var','right_hue_var']
    '''
    if hue_left_right:

        for xtick_i, xtick in enumerate(ax.get_xticklabels()):
            
#             for h in hue_left_right
            ax.text(xtick_i-.2, medians.loc[(xtick.get_text(),hue_left_right[0])]+vertical_offset, round(medians.loc[(xtick.get_text(),hue_left_right[0])],round_by),  horizontalalignment='center',  size='small', color=fontcolor, weight='semibold')
            ax.text(xtick_i+.2, medians.loc[(xtick.get_text(),hue_left_right[1])]+vertical_offset, round(medians.loc[(xtick.get_text(),hue_left_right[1])],round_by), horizontalalignment='center', size='small', color=fontcolor, weight='semibold')

    else:
        for xtick_i, xtick in enumerate(ax.get_xticklabels()):
            xtick = xtick.get_text()
            ax.text(xtick_i, medians[xtick] + vertical_offset, round(medians[xtick],round_by), 
                    horizontalalignment='center',size='small',color=fontcolor,weight='semibold')


