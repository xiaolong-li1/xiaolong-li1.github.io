from graphviz import Digraph

dot = Digraph(comment='Welcome Function Flowchart')

# 设置字体为支持中文的字体
dot.attr(fontname='SimSun')

# Nodes
dot.node('A', 'Start', fontname='SimSun')
dot.node('B', '进入welcome阶段', fontname='SimSun')
dot.node('C', '人脸检测唤醒', fontname='SimSun')
dot.node('D', '检测到大人脸?', fontname='SimSun')
dot.node('E', '迎宾词', fontname='SimSun')
dot.node('F', '语音唤醒', fontname='SimSun')
dot.node('G', '检测到语音输入?', fontname='SimSun')
dot.node('H', '被打断?', fontname='SimSun')
dot.node('I', '人脸识别迎宾语', fontname='SimSun')
dot.node('J', '统计识别到的人脸次数', fontname='SimSun')
dot.node('K', '筛选常见人脸', fontname='SimSun')
dot.node('L', '生成迎宾语', fontname='SimSun')
dot.node('M', 'End', fontname='SimSun')

# Edges
dot.edge('A', 'B')
dot.edge('B', 'C')
dot.edge('C', 'D')
dot.edge('D', 'E', label='是', fontname='SimSun')
dot.edge('D', 'F', label='否', fontname='SimSun')
dot.edge('E', 'F')
dot.edge('F', 'G')
dot.edge('G', 'H', label='是', fontname='SimSun')
dot.edge('G', 'I', label='否', fontname='SimSun')
dot.edge('H', 'I', label='是', fontname='SimSun')
dot.edge('H', 'F', label='否', fontname='SimSun')
dot.edge('I', 'J')
dot.edge('J', 'K')
dot.edge('K', 'L')
dot.edge('L', 'M')

# Save and render the graph
dot.render('welcome_function_flowchart', format='pdf', view=True)