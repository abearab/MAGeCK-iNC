import pandas as pd
print ('counts files (seperate by ,): ')
files = raw_input('-->')
print ('sample names (seperate by ,): ')
sample_names = raw_input('-->')
print ('output folder: ')
out_put = raw_input('-->')
print ('name: ')
name = raw_input('-->')

count_files =  files.split(',')
sample_names = sample_names.split(',')
dfs = []
for i,count_file in enumerate(count_files):
	df = pd.read_table(count_file,names =['sgRNA',sample_names[i]])
	dfs.append(df)
df_merge = reduce(lambda x, y: pd.merge(x, y, on = 'sgRNA'), dfs).fillna(0.0)
df_merge['Gene'] =df_merge['sgRNA'].apply(lambda x:x.split('_')[0] if (x.split('_')[2].endswith('-P1P2')) else  x.split('_')[0] + '_' + x.split('_')[2].split('-')[-1] )
cols = df_merge.columns.tolist()
cols = [cols[0]]+[cols[-1]] + cols[1:-1]
df_merge = df_merge[cols]
df_merge.to_csv(out_put+'/%s_merged_counts.txt'%name,sep = '\t',index=False)
