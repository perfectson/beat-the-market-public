from zipline.data.bundles import register, custom_stock_data, custom_index_data

register(' etf_bundle ', custom_stock_data . custom_stock_data ,
        calendar_name='NYSE')


register('index_bundle', custom_index_data . custom_index_data ,
        calendar_name='NYSE')
