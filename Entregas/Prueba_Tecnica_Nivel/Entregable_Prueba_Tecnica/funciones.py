from librerias import *
def visualizacion_datos(data_df):

    if data_df.columns.str.contains("target").any():
        data = data_df.columns.drop("target")
    else:
        data = data_df.columns
    for col in data:

        mean = data_df[col].mean()
        mode = data_df[col].mode()
        median = data_df[col].median()
        Percentil_25 = data_df[col].quantile(0.25)
        Percentil_75 = data_df[col].quantile(0.75)

        fig, axs = plt.subplots(1,2,figsize=(12,6))
        
        fig.suptitle(col)
        sns.histplot(data_df[col], kde=True, ax=axs[0])
        axs[0].axvline(mean, color="red", linestyle="--", label="Mean")
        axs[0].axvline(median, color="green", linestyle="--", label="Median")
        axs[0].axvline(mode[0], color="blue", linestyle="--", label="Mode")
        axs[0].axvline(Percentil_25, color="yellow", linestyle="--", label="25th Percentile")
        axs[0].axvline(Percentil_75, color="yellow", linestyle="--", label="75th Percentile")
        axs[0].legend(loc='upper right')

        axs[0].set_title("Histograma")
        sns.boxplot(data_df[col], ax=axs[1])
        axs[1].set_title("Boxplot")
        plt.tight_layout()
        plt.show()
