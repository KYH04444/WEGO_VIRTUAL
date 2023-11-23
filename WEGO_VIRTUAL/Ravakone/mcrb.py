import numpy as np
import matplotlib.pyplot as plt
from collections import deque

def distance(myXY, wayXY):
    return ((myXY[0]-wayXY[0])**2+(myXY[1]-wayXY[1])**2)**0.5


angle_increment = 0.01745329238474369
# org_ranges = [4.0312371253967285, 4.053857326507568, 1.8935692310333252, 1.8795140981674194, 4.326189041137695, 4.337224960327148, 10.0, 4.49317741394043, 5.458597183227539, 1.8064279556274414, 1.7970247268676758, 10.0, 4.69183349609375, 5.510079860687256, 1.6343741416931152, 1.626909852027893, 1.6316297054290771, 6.070561408996582, 4.847426891326904, 6.633082866668701, 4.9800848960876465, 1.4402337074279785, 1.4383970499038696, 5.242879390716553, 5.441957950592041, 5.614419937133789, 5.9762654304504395, 6.328234672546387, 1.2168326377868652, 1.217805027961731, 10.0, 10.0, 1.0502427816390991, 1.0425739288330078, 1.045011043548584, 1.0502692461013794, 10.0, 10.0, 0.9058425426483154, 0.8770340085029602, 0.8799300789833069, 0.883523166179657, 10.0, 10.0, 0.7659335136413574, 0.7318457365036011, 0.7287695407867432, 0.7335712313652039, 0.738663375377655, 0.7499776482582092, 10.0, 10.0, 10.0, 0.6403171420097351, 0.619358241558075, 0.6074384450912476, 0.6091770529747009, 0.6155022382736206, 0.6221526265144348, 0.6334499716758728, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 0.5114807486534119, 0.5012888312339783, 0.49164146184921265, 0.48471182584762573, 0.48472604155540466, 0.49151524901390076, 0.5004406571388245, 0.5098546743392944, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 0.41342151165008545, 0.4098855257034302, 0.40665552020072937, 0.4035981595516205, 0.40070676803588867, 0.39949530363082886, 0.4025396704673767, 0.4176751971244812, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 0.4133928120136261, 0.4087081849575043, 0.4086357653141022, 0.4090941548347473, 0.40967848896980286, 0.41039058566093445, 0.4115717113018036, 0.41875919699668884, 10.0, 10.0, 10.0, 10.0, 4.041809558868408, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 0.5323654413223267, 0.5143051147460938, 0.5113546848297119, 0.5147613883018494, 0.519059419631958, 0.5235909223556519, 0.532231867313385, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 0.6947166919708252, 0.681685745716095, 0.6815358400344849, 0.6919808983802795, 0.7037414312362671, 9.341429710388184, 0.9058883190155029, 0.891004204750061, 0.8878297805786133, 0.9043336510658264, 1.082696795463562, 1.0685391426086426, 1.079634428024292, 8.30145263671875, 8.198254585266113, 8.10002613067627, 8.0065336227417, 7.9175591468811035, 7.832900047302246, 4.593636512756348, 2.955409526824951, 7.603002071380615, 7.533855438232422, 7.468210220336914, 2.751676082611084, 7.34691047668457, 7.291020393371582, 2.5223493576049805, 7.1882429122924805, 7.141165733337402, 2.2904715538024902, 2.2795042991638184, 7.016188144683838, 6.979707717895508, 4.118997097015381, 2.0461363792419434, 6.8849358558654785, 1.8659472465515137, 6.833471298217773, 4.033658504486084, 6.790981292724609, 1.6882864236831665, 1.6933175325393677, 6.743505954742432, 3.941143274307251, 3.9747960567474365, 1.4936397075653076, 1.5109390020370483, 3.9628326892852783, 6.704967975616455, 6.705723762512207, 6.708524227142334, 1.310072422027588, 1.2987570762634277, 1.3020485639572144, 6.740296840667725, 6.753442287445068, 6.768707275390625, 6.786112308502197, 6.805685997009277, 6.827457427978516, 1.148226022720337, 1.1114505529403687, 1.115322470664978, 6.937284469604492, 6.970646381378174, 7.006479263305664, 7.044836044311523, 7.085788249969482, 7.129402160644531, 4.215209007263184, 7.224930286407471, 0.9347822070121765, 0.9359813332557678, 0.9431098103523254, 7.451728343963623, 7.516488552093506, 4.447758197784424, 7.656539440155029, 7.732120513916016, 7.811610698699951, 0.8118128776550293, 0.7889659404754639, 0.7819483280181885, 0.7897539734840393, 0.7992830276489258, 8.3812255859375, 8.493697166442871, 8.611889839172363, 5.134415626525879, 8.866716384887695, 9.00406265258789, 5.324669361114502, 9.300664901733398, 0.7143474817276001, 0.7012021541595459, 0.6899886727333069, 0.6910122036933899, 0.7032768130302429, 0.7172788977622986, 9.161428451538086, 6.2962188720703125, 6.434728622436523, 6.583462238311768, 6.74261474609375, 6.84137487411499, 6.798444747924805, 8.369762420654297, 8.27742862701416, 0.6118172407150269, 0.6049317121505737, 0.5989736914634705, 0.5934646725654602, 0.5944555401802063, 0.6104410290718079, 7.746634483337402, 7.685431003570557, 6.0916218757629395, 7.5727128982543945, 7.520986557006836, 7.472226142883301, 5.913736343383789, 7.383249282836914, 7.342877388000488, 7.305158615112305, 7.2700300216674805, 7.237430095672607, 7.207306385040283, 0.5429244637489319, 0.5394522547721863, 0.5377000570297241, 0.536122739315033, 0.5347169041633606, 0.5382716059684753, 5.677160263061523, 7.050479412078857, 7.0409321784973145, 7.0335540771484375, 7.028322696685791, 7.025245189666748, 7.024302959442139, 7.025501251220703, 5.61329984664917, 7.0343337059021, 7.0419793128967285, 7.051790714263916, 7.063779830932617, 7.077975273132324, 0.5651111006736755, 0.544185996055603, 0.543857753276825, 0.5456098914146423, 0.5475398898124695, 0.5496518611907959, 0.5591358542442322, 5.852569580078125, 7.309599876403809, 7.347635746002197, 7.388333797454834, 5.935500621795654, 5.9288201332092285, 7.527109146118164, 7.57919979095459, 7.634357452392578, 0.6377079486846924, 0.6133860945701599, 0.5991597175598145, 0.5997218489646912, 0.6051827669143677, 0.6109316349029541, 0.6174997091293335, 2.2989330291748047, 2.0702319145202637, 1.906118631362915, 1.8901983499526978, 3.3946104049682617, 0.7384295463562012, 0.7211949229240417, 0.7123159766197205, 0.7181599736213684, 0.7284903526306152, 0.741113007068634, 0.9071753025054932, 0.8913124799728394, 0.8952283263206482, 0.9100949168205261, 1.0330731868743896, 1.0176914930343628, 1.0255235433578491, 1.0459163188934326, 1.1959384679794312, 1.1862382888793945, 1.2086238861083984, 2.3342041969299316, 2.320249080657959, 3.4380202293395996, 3.5937066078186035, 2.1522741317749023, 2.1324639320373535, 3.724780321121216, 3.7334060668945312, 2.0223898887634277, 2.003798723220825, 10.0]
org_ranges = [1.094899296760559, 1.1189278364181519, 2.807621717453003, 2.822510242462158, 10.0, 3.0101184844970703, 0.9629978537559509, 0.952964186668396, 0.9452968239784241, 0.9608979225158691, 3.128147840499878, 10.0, 3.2197751998901367, 4.357246398925781, 3.3868772983551025, 3.365469217300415, 4.465743541717529, 10.0, 3.545894145965576, 0.8648503422737122, 0.8580067157745361, 0.853100061416626, 0.8507700562477112, 0.8809135556221008, 10.0, 3.7340667247772217, 10.0, 4.69207763671875, 10.0, 3.8230319023132324, 5.132288455963135, 3.917297124862671, 0.6907748579978943, 0.6896342635154724, 0.6887999176979065, 0.6881769895553589, 0.6991493105888367, 10.0, 4.326193332672119, 4.529779434204102, 4.707223415374756, 5.076120376586914, 5.660582065582275, 5.9435529708862305, 6.201986312866211, 6.369781970977783, 6.531578063964844, 9.311185836791992, 10.0, 10.0, 0.5459051132202148, 0.5403911471366882, 0.5421940088272095, 0.5447414517402649, 0.5474802851676941, 0.5508549213409424, 10.0, 10.0, 10.0, 9.864089012145996, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 0.45910075306892395, 0.4486444890499115, 0.4397425949573517, 0.43131566047668457, 0.42793703079223633, 0.4295184016227722, 0.43651312589645386, 0.44448330998420715, 0.4528907239437103, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 0.4161580502986908, 0.41180160641670227, 0.40877029299736023, 0.40590527653694153, 0.4032023549079895, 0.40113118290901184, 0.4027459919452667, 0.4140031635761261, 0.43838411569595337, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 0.46182093024253845, 0.45697876811027527, 0.45690223574638367, 0.4571206271648407, 0.4574788808822632, 0.45797765254974365, 0.46217769384384155, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 0.5703694820404053, 0.5417383313179016, 0.5362734198570251, 0.5384290218353271, 0.542057991027832, 0.5459042191505432, 0.5527618527412415, 10.0, 10.0, 10.0, 10.0, 10.0, 0.669292688369751, 0.6540634036064148, 0.6544592380523682, 0.6616509556770325, 0.6692088842391968, 10.0, 10.0, 10.0, 10.0, 10.0, 0.8123629093170166, 0.7992916703224182, 0.8043572306632996, 0.8167882561683655, 10.0, 10.0, 10.0, 6.711167335510254, 0.9806710481643677, 0.969508171081543, 0.9823353290557861, 9.770081520080566, 9.636618614196777, 1.159633994102478, 1.1459254026412964, 1.1609580516815186, 1.3528834581375122, 1.3388376235961914, 1.3626803159713745, 2.599580764770508, 1.5807936191558838, 1.5711441040039062, 1.7981677055358887, 8.533191680908203, 3.88541579246521, 8.39077091217041, 8.325092315673828, 3.6912283897399902, 8.204169273376465, 5.237429618835449, 8.09643268585205, 8.047260284423828, 3.230890989303589, 7.957892894744873, 7.917540073394775, 3.000638961791992, 7.845157146453857, 2.840754985809326, 7.783483505249023, 2.6351537704467773, 7.732117176055908, 4.940823078155518, 2.430905342102051, 4.8784098625183105, 7.659073352813721, 2.232133150100708, 2.2184789180755615, 7.629397392272949, 7.6241936683654785, 7.621314525604248, 2.000479221343994, 7.622526168823242, 7.62661600112915, 7.6330389976501465, 1.7781883478164673, 7.652915954589844, 7.6664042472839355, 1.5780712366104126, 1.5890679359436035, 7.721318244934082, 1.419765830039978, 1.40727961063385, 1.4147285223007202, 1.2170050144195557, 1.2142034769058228, 1.2198125123977661, 1.0161067247390747, 1.0176093578338623, 1.023007869720459, 0.861250638961792, 0.8281420469284058, 0.8287816047668457, 0.8343113660812378, 0.843048095703125, 0.6814072728157043, 0.6604164838790894, 0.6592772006988525, 0.6648792624473572, 0.670783519744873, 5.572001934051514, 8.822874069213867, 5.652031421661377, 9.011863708496094, 0.5494601130485535, 0.5347215533256531, 0.5214465260505676, 0.5180827975273132, 0.5218442678451538, 0.5286806225776672, 0.5358638167381287, 6.306060314178467, 6.397622585296631, 6.495792865753174, 6.599918842315674, 9.828731536865234, 9.652381896972656, 9.485092163085938, 9.326294898986816, 7.197067737579346, 9.032160758972168, 8.895922660827637, 8.766365051269531, 8.643122673034668, 0.480357825756073, 0.4734439253807068, 0.46720007061958313, 0.46125778555870056, 0.4577311873435974, 0.4595910608768463, 0.4699796438217163, 0.4831641614437103, 7.770233631134033, 6.045148849487305, 7.624046802520752, 7.556404113769531, 7.492212295532227, 7.431351184844971, 7.37369441986084, 5.8263373374938965, 7.267584800720215, 0.4527585208415985, 0.44846487045288086, 0.4457544684410095, 0.4432123303413391, 0.44083067774772644, 0.43921688199043274, 0.4426644444465637, 0.46509161591529846, 6.925060272216797, 6.8993096351623535, 6.875837326049805, 5.3885498046875, 6.835579872131348, 5.3910369873046875, 6.8040313720703125, 6.7914605140686035, 6.780997276306152, 6.772625923156738, 6.766332149505615, 6.762111663818359, 6.759952545166016, 5.342377662658691, 0.4830459654331207, 0.48080945014953613, 0.4812270700931549, 0.4817923605442047, 0.4825080335140228, 0.4835999011993408, 0.49239781498908997, 0.6765928864479065, 0.6760307550430298, 0.6780810356140137, 0.6803536415100098, 0.6858683824539185, 2.2205193042755127, 2.1833503246307373, 7.0131306648254395, 2.367779493331909, 7.085803508758545, 7.125987529754639, 2.5529980659484863, 2.5499184131622314, 7.262763023376465, 2.7214179039001465, 2.7050728797912598, 5.921117305755615, 7.486198425292969, 5.969239234924316, 2.9077701568603516, 6.131406784057617, 7.762831211090088, 3.1509287357330322, 3.149934768676758, 6.388385772705078, 6.460845947265625, 3.2972822189331055, 1.8198927640914917, 1.7802743911743164, 1.6316856145858765, 1.6271800994873047, 1.6535296440124512, 1.4726643562316895, 1.4663608074188232, 1.489465355873108, 2.429290771484375, 1.280192494392395, 1.2567991018295288, 1.250908374786377, 1.2733622789382935, 2.5714356899261475, 10.0, 1.1150288581848145, 1.0993971824645996]

X = []
Y = []

for i in range(len(org_ranges)):
    x = org_ranges[i]*np.cos(angle_increment*i)
    y = org_ranges[i]*np.sin(angle_increment*i)
    if distance([0,0], [x,y])<3:
        X.append(x)
        Y.append(y)
plt.plot(X,Y,'bo')


# 1. 한 개의 라바콘에서 한 개만 검출 (0.1)
# 2. 라바콘 주변에 간격이 0.4 이하인 가장 가까운 라바콘 찾기

sa = 130
ranges = org_ranges[360-sa:360] + org_ranges[0:sa]

ALL_XY = []
ROI_TXY = []
for i in range(len(ranges)):
    x = ranges[i]*np.cos(angle_increment*i)
    y = ranges[i]*np.sin(angle_increment*i)
    ALL_XY.append([x,y])
    if distance([0,0], [x,y])<3:
        ROI_TXY.append([i,x,y])

RB_TXY = [ROI_TXY[0]]
Angle_Relation = {}
Angle_Relation[ROI_TXY[0][0]]=[]
for i in range(len(ROI_TXY)):
    fac=True
    for j in range(len(RB_TXY)):
        # 라바콘 크기 0.1 이하
        if distance([RB_TXY[j][1], RB_TXY[j][2]], [ROI_TXY[i][1],ROI_TXY[i][2]])<0.1:
            fac=False
    if fac:
        RB_TXY.append(ROI_TXY[i])
        Angle_Relation[ROI_TXY[i][0]] = []

for i in range(len(RB_TXY)):
    for j in range(i+1,len(RB_TXY)):
        # 라바콘 주변 간격 0.4 이하
        if distance([RB_TXY[i][1],RB_TXY[i][2]], [RB_TXY[j][1],RB_TXY[j][2]])<0.4:
            # print(RB_TXY[i][0],RB_TXY[j][0])
            Angle_Relation[RB_TXY[i][0]].append(RB_TXY[j][0])
            Angle_Relation[RB_TXY[j][0]].append(RB_TXY[i][0])


def dfs(start, visited=[]):
    global Angle_Relation, mc_visited
    visited.append(start)
    mc_visited[start] = True
    for node in Angle_Relation[start]:
        if node not in visited:
            mc_visited[start] = True
            dfs(node, visited)
    return visited


mc_visited = [False for _ in range(sa*2)]
Lidar_Correction = []
for i in range(len(RB_TXY)):
    if mc_visited[RB_TXY[i][0]]==False:
        temp = dfs(RB_TXY[i][0],[])
        if len(temp)>2:
            Lidar_Correction.append(dfs(temp[-1],[]))

CORRECTION_TXY = []
for relation_list in Lidar_Correction:
    relation_list.sort()
    for i in range(len(relation_list)-1):
        ang_s, x_s, y_s = relation_list[i], ALL_XY[relation_list[i]][0], ALL_XY[relation_list[i]][1]
        ang_e, x_e, y_e = relation_list[i+1], ALL_XY[relation_list[i+1]][0], ALL_XY[relation_list[i+1]][1]
        for j in range(ang_s+1,ang_e):
            corr_x = x_s + (x_e-x_s)*((j-ang_s)/(ang_e-ang_s))
            corr_y = y_s + (y_e-y_s)*((j-ang_s)/(ang_e-ang_s))
            ALL_XY[j] = [corr_x, corr_y]
            CORRECTION_TXY.append([j, corr_x, corr_y])
          
# ranges = org_ranges[240:360] + org_ranges[0:120]
for i in range(len(CORRECTION_TXY)):
    angle = CORRECTION_TXY[i][0]
    x = CORRECTION_TXY[i][1]
    y = CORRECTION_TXY[i][2]
    if angle<sa:
        org_ranges[360-sa+angle] = distance([0,0], [x,y])
    else:
        org_ranges[angle-sa] = distance([0,0], [x,y])


# # Visualization
# XY = []
# for i in range(len(org_ranges)):
#     x = org_ranges[i]*np.cos(angle_increment*i)
#     y = org_ranges[i]*np.sin(angle_increment*i)
#     XY.append([x,y])

# for i in range(len(XY)):
#     plt.plot(XY[i][0], XY[i][1], 'ro')

# plt.xlim([-3, 3])
# plt.ylim([-3, 3])
# plt.show()
