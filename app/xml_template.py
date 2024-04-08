template_xml_without_values = """
<?xml version="1.0" encoding="UTF-8"?>
    <d2:payload
        modelBaseVersion="3"
        lang="FR"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xmlns:d2="http://datex2.eu/schema/3/d2Payload"
        xmlns:com="http://datex2.eu/schema/3/common"
        xmlns:comx="http://datex2.eu/schema/3/commonExtension"
        xmlns:loc="http://datex2.eu/schema/3/locationReferencing"
        xmlns:locdx="https://raw.githubusercontent.com/MTES-MCT/dialog/main/docs/spec/datex2"
        xmlns="http://datex2.eu/schema/3/trafficRegulation"
        xsi:schemaLocation="http://datex2.eu/schema/3/d2Payload DATEXII_3_D2Payload.xsd"
        xsi:type="TrafficRegulationPublication"
        id="910928b3-58a1-4462-881b-53dec84602f9"
    >
    <com:publicationTime></com:publicationTime>
    <com:publicationCreator>
        <com:country></com:country>
        <com:nationalIdentifier></com:nationalIdentifier>
    </com:publicationCreator>

    <trafficRegulationsFromCompetentAuthorities>
        <trafficRegulationOrder id="064ca240-2b58-73ea-8000-2d03faf5d44c" version="1">
    <description>
        <com:values>
            <com:value lang="fr"></com:value>
        </com:values>
    </description>

    <issuingAuthority>
        <com:values>
            <com:value lang="fr"></com:value>
        </com:values>
    </issuingAuthority>

    <regulationId></regulationId>
    <status></status>

    <trafficRegulation>
        <status></status>

        <typeOfRegulation xsi:type="AccessRestriction">
            <accessRestrictionType></accessRestrictionType>
        </typeOfRegulation>

        <condition xsi:type="ConditionSet">
            <operator></operator>

            <conditions xsi:type="ValidityCondition">
                <validityByOrder>
                    <com:validityStatus></com:validityStatus>
                    <com:validityTimeSpecification>
                        <com:overallStartTime></com:overallStartTime>
                        <com:overallEndTime></com:overallEndTime>
                    </com:validityTimeSpecification>
                </validityByOrder>
            </conditions>

            <conditions xsi:type="LocationCondition">
                <locationByOrder xsi:type="loc:SingleRoadLinearLocation">
                    <loc:linearWithinLinearElement>
                        <loc:linearElement xsi:type="loc:LinearElement">
                            <loc:roadName>
                                <com:values>
                                    <com:value lang="fr"></com:value>
                                </com:values>
                            </loc:roadName>
                        </loc:linearElement>

                        <loc:fromPoint xsi:type="loc:DistanceFromLinearElementReferent">
                            <loc:distanceAlong>0</loc:distanceAlong>
                            <loc:fromReferent>
                                <loc:referentIdentifier></loc:referentIdentifier>
                                <loc:referentName></loc:referentName>
                                <loc:referentType></loc:referentType>
                                <loc:pointCoordinates>
                                    <loc:latitude></loc:latitude>
                                    <loc:longitude></loc:longitude>
                                </loc:pointCoordinates>
                            </loc:fromReferent>
                        </loc:fromPoint>
                        <loc:toPoint xsi:type="loc:DistanceFromLinearElementReferent">
                            <loc:distanceAlong></loc:distanceAlong>
                            <loc:fromReferent>
                                <loc:referentIdentifier></loc:referentIdentifier>
                                <loc:referentName></loc:referentName>
                                <loc:referentType></loc:referentType>
                                <loc:pointCoordinates>
                                    <loc:latitude></loc:latitude>
                                    <loc:longitude></loc:longitude>
                                </loc:pointCoordinates>
                            </loc:fromReferent>
                        </loc:toPoint>
                    </loc:linearWithinLinearElement>
                </locationByOrder>
            </conditions>
        </condition>
    </trafficRegulation>
</trafficRegulationOrder>

<trafficRegulationOrder id="random-id" version="1">
    <description>
        <com:values>
            <com:value lang="fr"></com:value>
        </com:values>
    </description>

    <issuingAuthority>
        <com:values>
            <com:value lang="fr"></com:value>
        </com:values>
    </issuingAuthority>

    <regulationId></regulationId>
    <status></status>

    <trafficRegulation>
        <status></status>

        <typeOfRegulation xsi:type="AccessRestriction">
            <accessRestrictionType></accessRestrictionType>
        </typeOfRegulation>

        <condition xsi:type="ConditionSet">
            <operator></operator>

            <conditions xsi:type="ConditionSet">
                <operator></operator>
                <conditions xsi:type="ValidityCondition">
                    <validityByOrder>
                        <com:validityStatus></com:validityStatus>
                        <com:validityTimeSpecification>
                            <com:overallStartTime></com:overallStartTime>
                            <com:overallEndTime></com:overallEndTime>
                        </com:validityTimeSpecification>
                    </validityByOrder>
                </conditions>
                <conditions xsi:type="ValidityCondition">
                    <validityByOrder>
                        <com:validityStatus></com:validityStatus>
                        <com:validityTimeSpecification>
                            <com:overallStartTime></com:overallStartTime>
                            <com:overallEndTime></com:overallEndTime>
                        </com:validityTimeSpecification>
                    </validityByOrder>
                </conditions>
                <conditions xsi:type="ValidityCondition">
                    <validityByOrder>
                        <com:validityStatus></com:validityStatus>
                        <com:validityTimeSpecification>
                            <com:overallStartTime></com:overallStartTime>
                            <com:overallEndTime></com:overallEndTime>
                        </com:validityTimeSpecification>
                    </validityByOrder>
                </conditions>
                <conditions xsi:type="ValidityCondition">
                    <validityByOrder>
                        <com:validityStatus></com:validityStatus>
                        <com:validityTimeSpecification>
                            <com:overallStartTime></com:overallStartTime>
                            <com:overallEndTime></com:overallEndTime>
                        </com:validityTimeSpecification>
                    </validityByOrder>
                </conditions>
                <conditions xsi:type="ValidityCondition">
                    <validityByOrder>
                        <com:validityStatus></com:validityStatus>
                        <com:validityTimeSpecification>
                            <com:overallStartTime></com:overallStartTime>
                            <com:overallEndTime></com:overallEndTime>
                        </com:validityTimeSpecification>
                    </validityByOrder>
                </conditions>
                <conditions xsi:type="ValidityCondition">
                    <validityByOrder>
                        <com:validityStatus></com:validityStatus>
                        <com:validityTimeSpecification>
                            <com:overallStartTime></com:overallStartTime>
                            <com:overallEndTime></com:overallEndTime>
                        </com:validityTimeSpecification>
                    </validityByOrder>
                </conditions>
            </conditions>

            <conditions xsi:type="ConditionSet">
                <operator></operator>
                <conditions xsi:type="LocationCondition">
                    <locationByOrder xsi:type="loc:SingleRoadLinearLocation">
                        <loc:linearWithinLinearElement>
                            <loc:linearElement xsi:type="loc:LinearElement">
                                <loc:roadName>
                                    <com:values>
                                        <com:value lang="fr"></com:value>
                                    </com:values>
                                </loc:roadName>
                            </loc:linearElement>
                            <loc:fromPoint xsi:type="loc:DistanceFromLinearElementReferent">
                                <loc:distanceAlong></loc:distanceAlong>
                                <loc:fromReferent>
                                    <loc:referentIdentifier></loc:referentIdentifier>
                                    <loc:referentName></loc:referentName>
                                    <loc:referentType></loc:referentType>
                                    <loc:pointCoordinates>
                                        <loc:latitude></loc:latitude>
                                        <loc:longitude></loc:longitude>
                                    </loc:pointCoordinates>
                                </loc:fromReferent>
                            </loc:fromPoint>
                            <loc:toPoint xsi:type="loc:DistanceFromLinearElementReferent">
                                <loc:distanceAlong></loc:distanceAlong>
                                <loc:fromReferent>
                                    <loc:referentIdentifier></loc:referentIdentifier>
                                    <loc:referentName></loc:referentName>
                                    <loc:referentType></loc:referentType>
                                    <loc:pointCoordinates>
                                        <loc:latitude></loc:latitude>
                                        <loc:longitude></loc:longitude>
                                    </loc:pointCoordinates>
                                </loc:fromReferent>
                            </loc:toPoint>
                        </loc:linearWithinLinearElement>
                    </locationByOrder>
                </conditions>

                <conditions xsi:type="LocationCondition">
                    <locationByOrder xsi:type="loc:SingleRoadLinearLocation">
                        <loc:linearWithinLinearElement>
                            <loc:linearElement xsi:type="loc:LinearElement">
                                <loc:roadName>
                                    <com:values>
                                        <com:value lang="fr"></com:value>
                                    </com:values>
                                </loc:roadName>
                            </loc:linearElement>
                            <loc:fromPoint xsi:type="loc:DistanceFromLinearElementReferent">
                                <loc:distanceAlong></loc:distanceAlong>
                                <loc:fromReferent>
                                    <loc:referentIdentifier></loc:referentIdentifier>
                                    <loc:referentName></loc:referentName>
                                    <loc:referentType></loc:referentType>
                                    <loc:pointCoordinates>
                                        <loc:latitude></loc:latitude>
                                        <loc:longitude></loc:longitude>
                                    </loc:pointCoordinates>
                                </loc:fromReferent>
                            </loc:fromPoint>
                            <loc:toPoint xsi:type="loc:DistanceFromLinearElementReferent">
                                <loc:distanceAlong></loc:distanceAlong>
                                <loc:fromReferent>
                                    <loc:referentIdentifier></loc:referentIdentifier>
                                    <loc:referentName></loc:referentName>
                                    <loc:referentType></loc:referentType>
                                    <loc:pointCoordinates>
                                        <loc:latitude></loc:latitude>
                                        <loc:longitude></loc:longitude>
                                    </loc:pointCoordinates>
                                </loc:fromReferent>
                            </loc:toPoint>
                        </loc:linearWithinLinearElement>
                    </locationByOrder>
                </conditions>

                <conditions xsi:type="LocationCondition">
                    <locationByOrder xsi:type="loc:SingleRoadLinearLocation">
                        <loc:linearWithinLinearElement>
                            <loc:linearElement xsi:type="loc:LinearElement">
                                <loc:roadName>
                                    <com:values>
                                        <com:value lang="fr"></com:value>
                                    </com:values>
                                </loc:roadName>
                            </loc:linearElement>
                            <loc:fromPoint xsi:type="loc:DistanceFromLinearElementReferent">
                                <loc:distanceAlong></loc:distanceAlong>
                                <loc:fromReferent>
                                    <loc:referentIdentifier></loc:referentIdentifier>
                                    <loc:referentName></loc:referentName>
                                    <loc:referentType></loc:referentType>
                                    <loc:pointCoordinates>
                                        <loc:latitude></loc:latitude>
                                        <loc:longitude></loc:longitude>
                                    </loc:pointCoordinates>
                                </loc:fromReferent>
                            </loc:fromPoint>
                            <loc:toPoint xsi:type="loc:DistanceFromLinearElementReferent">
                                <loc:distanceAlong></loc:distanceAlong>
                                <loc:fromReferent>
                                    <loc:referentIdentifier></loc:referentIdentifier>
                                    <loc:referentName></loc:referentName>
                                    <loc:referentType></loc:referentType>
                                    <loc:pointCoordinates>
                                        <loc:latitude></loc:latitude>
                                        <loc:longitude></loc:longitude>
                                    </loc:pointCoordinates>
                                </loc:fromReferent>
                            </loc:toPoint>
                        </loc:linearWithinLinearElement>
                    </locationByOrder>
                </conditions>

                <conditions xsi:type="LocationCondition">
                    <locationByOrder xsi:type="loc:SingleRoadLinearLocation">
                        <loc:linearWithinLinearElement>
                            <loc:linearElement xsi:type="loc:LinearElement">
                                <loc:roadName>
                                    <com:values>
                                        <com:value lang="fr"></com:value>
                                    </com:values>
                                </loc:roadName>
                            </loc:linearElement>
                            <loc:fromPoint xsi:type="loc:PercentageDistanceAlongLinearElement">
                                <loc:percentageDistanceAlong></loc:percentageDistanceAlong>
                            </loc:fromPoint>
                            <loc:toPoint xsi:type="loc:PercentageDistanceAlongLinearElement">
                                <loc:percentageDistanceAlong></loc:percentageDistanceAlong>
                            </loc:toPoint>
                        </loc:linearWithinLinearElement>
                    </locationByOrder>
                </conditions>
            </conditions>

            <conditions xsi:type="DriverCondition">
                <negate></negate>
                <driverCharacteristicsType></driverCharacteristicsType>
            </conditions>
        </condition>
    </trafficRegulation>
</trafficRegulationOrder>

    </trafficRegulationsFromCompetentAuthorities>
</d2:payload>
"""

template_xml_without_values_embedding = [-0.03564453125, 0.03265380859375, 0.0228729248046875, 0.0195159912109375, 0.0546875, 0.034210205078125, 0.032928466796875, -0.02569580078125, -0.0100250244140625, 0.003543853759765625, -0.01331329345703125, 0.06427001953125, -0.003620147705078125, -0.008880615234375, -0.057220458984375, 0.0290985107421875, 0.01029205322265625, 0.0047454833984375, 0.0099334716796875, -0.016632080078125, -0.039825439453125, -0.0212554931640625, -0.044891357421875, 0.010894775390625, -0.058197021484375, -0.0232696533203125, -0.0167388916015625, -0.0268096923828125, -0.03143310546875, 0.0177154541015625, 0.04888916015625, 0.003704071044921875, 0.0011587142944335938, -0.0307159423828125, 0.013214111328125, -0.037384033203125, -0.015533447265625, -0.043792724609375, 0.0413818359375, 0.01267242431640625, -0.0199737548828125, -0.023651123046875, 0.01049041748046875, -0.00447845458984375, -0.03692626953125, -0.007030487060546875, 0.0112762451171875, -0.00701141357421875, 0.021087646484375, -0.038665771484375, 0.03204345703125, 0.040740966796875, 0.0303192138671875, -0.0034122467041015625, -0.006977081298828125, 0.050933837890625, -0.007740020751953125, 0.0253448486328125, -0.048828125, 0.039886474609375, -0.040252685546875, 0.0208740234375, -0.0225677490234375, -0.004421234130859375, 0.0504150390625, 0.004352569580078125, 0.005603790283203125, -0.005008697509765625, -0.046600341796875, 0.007015228271484375, -0.01120758056640625, 0.0049896240234375, -0.0035572052001953125, 0.0142669677734375, -0.015716552734375, -0.0280609130859375, 0.023773193359375, 0.0217132568359375, 0.011566162109375, -0.00794219970703125, -0.036041259765625, -0.00476837158203125, 0.041534423828125, -0.0207366943359375, -0.00518798828125, 0.0154571533203125, 0.0203704833984375, -0.0090179443359375, -0.00864410400390625, 0.01861572265625, 0.032440185546875, -0.01097869873046875, 0.03369140625, -0.01113128662109375, 0.04119873046875, 0.056915283203125, -0.0209503173828125, 0.0311737060546875, -0.017242431640625, 0.03662109375, 0.0203094482421875, -0.0347900390625, 0.09088134765625, 0.0023784637451171875, 0.0007085800170898438, -0.018829345703125, 0.0114288330078125, 0.00244903564453125, 0.0036182403564453125, -0.040008544921875, -0.09539794921875, -0.030303955078125, -0.00647735595703125, -0.0227508544921875, -0.048980712890625, -0.0224761962890625, -0.007427215576171875, 0.03533935546875, -0.058349609375, -0.044097900390625, 0.00885772705078125, 0.054229736328125, -0.006862640380859375, 0.004974365234375, -0.036163330078125, -0.03009033203125, 0.03985595703125, 0.0200653076171875, -0.0130157470703125, -0.028350830078125, -0.02105712890625, 0.00756072998046875, -0.034393310546875, -0.04046630859375, -0.018798828125, 0.0111541748046875, 0.0194091796875, 0.018402099609375, -0.05511474609375, -0.00888824462890625, 0.00563812255859375, -0.031829833984375, -0.072998046875, -0.004138946533203125, -0.0367431640625, -0.014251708984375, -0.011566162109375, 0.03240966796875, -0.0102386474609375, 0.0008344650268554688, 0.00046539306640625, 0.031402587890625, 0.08062744140625, 0.0144805908203125, -0.0113067626953125, -0.0084381103515625, 0.0011911392211914062, 0.023468017578125, 0.062286376953125, 0.005939483642578125, -0.0163421630859375, 0.0152435302734375, 0.0290374755859375, 0.037322998046875, -0.0199737548828125, -0.04443359375, -0.0236053466796875, 0.013916015625, -0.006374359130859375, 0.01251983642578125, 0.03472900390625, -0.045806884765625, 0.041412353515625, 0.042999267578125, -0.0177764892578125, 0.018402099609375, 0.018524169921875, 0.007843017578125, 0.04632568359375, 0.040496826171875, 0.023681640625, -0.0196380615234375, 0.03985595703125, -0.007106781005859375, 0.03717041015625, -0.0181121826171875, -0.049835205078125, 0.020355224609375, -0.00949859619140625, 0.07147216796875, -0.037811279296875, -0.01226043701171875, -0.02197265625, 0.0408935546875, 0.00920867919921875, 0.069580078125, 0.0312042236328125, -0.0147552490234375, 0.04052734375, 0.0037593841552734375, 0.016265869140625, 0.016448974609375, -0.00032019615173339844, 0.0277557373046875, 0.06024169921875, -0.003131866455078125, -0.02947998046875, 0.04534912109375, 0.016632080078125, -0.0101776123046875, 0.0005841255187988281, 0.02655029296875, -0.042144775390625, -0.039398193359375, -0.05767822265625, -0.0267791748046875, -0.00016045570373535156, -0.0041046142578125, 0.0021495819091796875, -0.00428009033203125, 0.01313018798828125, 0.004486083984375, -0.00945281982421875, 0.0191650390625, -0.039154052734375, 0.049072265625, 0.01067352294921875, -0.00037384033203125, -0.02117919921875, -0.0018548965454101562, 0.00849151611328125, 0.01251983642578125, -0.0004787445068359375, -0.0051422119140625, -0.025909423828125, -0.004665374755859375, 0.01267242431640625, -0.0209808349609375, 0.0265045166015625, 0.00789642333984375, -0.0214080810546875, -0.008209228515625, -0.02734375, 0.008056640625, -0.0006399154663085938, -0.002445220947265625, -0.00557708740234375, -0.0226593017578125, 0.009063720703125, 0.0418701171875, -0.08636474609375, -0.0364990234375, -0.029998779296875, -0.002994537353515625, -0.041290283203125, -0.045257568359375, -0.0199737548828125, -0.03521728515625, 0.0286865234375, -0.0014057159423828125, 0.010833740234375, 0.004596710205078125, 0.0030612945556640625, -0.0321044921875, 0.017364501953125, 0.0156402587890625, 0.005588531494140625, 0.01483917236328125, 0.054534912109375, -0.0186920166015625, -0.03460693359375, -0.027069091796875, 0.05126953125, -0.0208282470703125, 0.0513916015625, -0.006336212158203125, -0.01293182373046875, 0.024871826171875, -0.01093292236328125, 0.0286865234375, -0.0013933181762695312, -0.004871368408203125, -0.031463623046875, 0.0171966552734375, -0.041717529296875, 0.0200347900390625, -0.02056884765625, 0.01293182373046875, -0.02532958984375, -0.034637451171875, 3.9696693420410156e-05, 0.0689697265625, 0.0094146728515625, -0.00867462158203125, -0.024627685546875, -0.005977630615234375, 0.0173492431640625, 0.006626129150390625, -0.0082244873046875, 0.024383544921875, 0.02899169921875, -0.029022216796875, -0.003021240234375, 0.0194091796875, 0.0450439453125, -0.058441162109375, -0.0200958251953125, -0.02252197265625, -0.018463134765625, -0.0562744140625, -0.01031494140625, -0.00502777099609375, 0.0035915374755859375, 0.046112060546875, -0.021942138671875, -0.00962066650390625, -0.039703369140625, -0.034942626953125, -0.0079498291015625, -0.03826904296875, -0.052490234375, -0.0005269050598144531, 0.087158203125, -0.00031447410583496094, 0.009490966796875, 0.005321502685546875, -0.0231170654296875, 0.001216888427734375, 0.00254058837890625, -0.016571044921875, 0.024169921875, -0.0159759521484375, 0.03076171875, 0.0125732421875, 0.018951416015625, 0.021087646484375, 0.061126708984375, 0.040374755859375, -0.045257568359375, -0.0130157470703125, 0.00853729248046875, 0.0132598876953125, 0.025787353515625, -0.004428863525390625, -0.0548095703125, -0.010345458984375, -0.02105712890625, 0.009552001953125, 0.02752685546875, 0.03289794921875, 0.003498077392578125, 0.001316070556640625, -0.0170135498046875, 0.057525634765625, -0.03631591796875, 0.0650634765625, -0.024749755859375, -0.05084228515625, 0.0242156982421875, 0.0404052734375, -0.028167724609375, 0.00182342529296875, 0.01468658447265625, 0.0020351409912109375, -0.01348114013671875, 0.05157470703125, -0.012969970703125, 0.0450439453125, -0.0137786865234375, -0.00344085693359375, -0.009063720703125, -0.021942138671875, 0.0063629150390625, 0.035125732421875, 0.0291748046875, 0.0199432373046875, 0.01129913330078125, -0.032196044921875, -0.02667236328125, -0.0021800994873046875, -0.052490234375, 0.004241943359375, 0.048553466796875, 0.00388336181640625, 0.004024505615234375, -0.002048492431640625, -0.081787109375, -0.005828857421875, -0.0174407958984375, 0.053466796875, 0.0673828125, 0.0243988037109375, 0.0233306884765625, 0.0167388916015625, -0.0158233642578125, 0.009918212890625, 0.016387939453125, 0.03826904296875, 0.046112060546875, -0.0006418228149414062, 0.00817108154296875, -0.02862548828125, 0.0318603515625, 0.046051025390625, 0.01175689697265625, -0.0119171142578125, 0.048828125, 0.042694091796875, 0.0245361328125, -0.01412200927734375, 0.04095458984375, -0.0003581047058105469, -0.0352783203125, -0.00011718273162841797, -0.0280914306640625, 0.0247802734375, -0.031341552734375, 0.00494384765625, -0.01458740234375, 0.0228271484375, -0.01983642578125, 0.0118408203125, -0.08013916015625, 0.010223388671875, 0.0293731689453125, -0.0281982421875, -0.028961181640625, 0.0279388427734375, 0.0012035369873046875, 0.034912109375, -0.073974609375, -0.0164794921875, 0.0404052734375, -0.03515625, -0.035919189453125, 0.00637054443359375, 0.040557861328125, -0.06573486328125, -0.0406494140625, -0.031890869140625, 0.0416259765625, 0.010711669921875, -0.0201263427734375, 0.061767578125, -0.0034923553466796875, 0.0073699951171875, 0.0287322998046875, 0.0174407958984375, -0.005290985107421875, 0.0030975341796875, 0.051605224609375, -0.00494384765625, -0.03900146484375, 0.0295562744140625, 0.005809783935546875, 0.0099639892578125, -0.046722412109375, -0.0232696533203125, 0.00274658203125, 0.0134429931640625, 0.025299072265625, -0.007755279541015625, -0.08416748046875, -0.042510986328125, -0.0169830322265625, 0.0283203125, 0.021331787109375, 0.0241241455078125, -0.025054931640625, -0.060791015625, 0.013946533203125, -0.021209716796875, -0.023651123046875, -0.00455474853515625, -0.0092926025390625, -0.02264404296875, 0.028289794921875, 0.048736572265625, -0.00531005859375, -0.029449462890625, 0.05596923828125, 0.003662109375, -0.00342559814453125, -0.04241943359375, 0.0489501953125, 0.0282745361328125, -0.06494140625, -0.021881103515625, -0.0205535888671875, 0.039031982421875, 0.035858154296875, -0.0576171875, -0.028289794921875, -0.034393310546875, -0.037353515625, -0.03594970703125, 0.01348114013671875, -0.01824951171875, -0.0302734375, 0.01068115234375, -0.0119476318359375, -0.003009796142578125, 0.0180206298828125, 0.01300048828125, -0.00015723705291748047, -0.01168060302734375, -0.025634765625, -0.038787841796875, 0.023193359375, -0.04534912109375, -0.00817108154296875, -0.01169586181640625, 0.0163116455078125, 0.0214385986328125, 0.01454925537109375, -0.01187896728515625, -0.052154541015625, 0.007427215576171875, -0.0022220611572265625, -0.01100921630859375, -0.02703857421875, -0.0302276611328125, -0.0386962890625, -0.0295562744140625, 0.00870513916015625, 0.00614166259765625, 0.0024852752685546875, -0.0122222900390625, 0.025787353515625, -0.0550537109375, 0.0132904052734375, 0.0294342041015625, -0.009552001953125, -0.009735107421875, -0.009490966796875, -0.0038547515869140625, 0.00043129920959472656, -0.0149688720703125, -0.007305145263671875, -0.0011072158813476562, -0.0872802734375, -0.0088043212890625, -0.0221405029296875, -0.039337158203125, -0.00962066650390625, -0.0108642578125, -0.07568359375, 0.028656005859375, 0.029022216796875, -0.0022563934326171875, 0.0236968994140625, -0.039276123046875, -0.0066375732421875, -0.022125244140625, -0.01483154296875, 0.0156402587890625, -0.0204925537109375, -4.655122756958008e-05, -0.0031528472900390625, -0.0562744140625, 0.0511474609375, 0.0384521484375, 0.056427001953125, -0.0160369873046875, 0.00780487060546875, -0.049102783203125, 0.0051116943359375, -0.00853729248046875, 0.007171630859375, -0.005573272705078125, -0.0302276611328125, 0.01114654541015625, -0.03143310546875, -0.00963592529296875, -0.0192108154296875, 0.037750244140625, -0.0147552490234375, -0.0188446044921875, -0.00548553466796875, 0.02655029296875, 0.00014603137969970703, 0.0265045166015625, -0.02056884765625, -0.05157470703125, 0.0295257568359375, -0.030914306640625, 0.05535888671875, 0.031494140625, 0.00017011165618896484, -0.01468658447265625, -0.01959228515625, 0.0090484619140625, -0.006481170654296875, -0.07501220703125, -0.0290679931640625, 0.01922607421875, -0.020721435546875, 0.04229736328125, 0.01070404052734375, 0.055816650390625, 0.0080413818359375, -0.004673004150390625, 0.01605224609375, 0.02960205078125, 0.054473876953125, -0.02313232421875, -0.0219573974609375, -0.03717041015625, 0.03271484375, -0.056396484375, -0.038970947265625, 0.0295867919921875, 0.0087432861328125, -0.0660400390625, -0.0262451171875, -0.038330078125, -0.0163726806640625, -0.007213592529296875, 0.01322174072265625, -0.0117645263671875, 0.039093017578125, 0.00506591796875, -0.0211944580078125, 0.0160675048828125, -0.011199951171875, 0.0099639892578125, 0.033538818359375, 0.027984619140625, 0.0308685302734375, 0.032958984375, 0.0024433135986328125, 0.039794921875, 0.007717132568359375, 0.028045654296875, 0.021881103515625, -0.0079193115234375, 0.03778076171875, 0.06658935546875, -0.02386474609375, -0.06280517578125, -0.0060577392578125, 0.0369873046875, 0.0360107421875, 0.04388427734375, 0.001842498779296875, -0.0104522705078125, -0.0007004737854003906, -0.0298309326171875, -0.0021495819091796875, 2.568960189819336e-05, 0.01971435546875, -0.009490966796875, -0.06256103515625, 0.03948974609375, -0.05413818359375, -0.002391815185546875, 0.0289154052734375, -0.0230712890625, 0.0300445556640625, 0.038787841796875, -0.016510009765625, -0.01318359375, 0.045928955078125, -0.0205841064453125, -0.019927978515625, -0.0625, -0.0236968994140625, 0.0276336669921875, -0.04541015625, -0.06500244140625, -0.0040435791015625, 0.0618896484375, -0.039398193359375, -0.032562255859375, -0.01006317138671875, 0.001682281494140625, 0.022064208984375, -0.0007534027099609375, -0.024322509765625, 0.0214996337890625, -0.0005779266357421875, -0.0303802490234375, 0.01273345947265625, 0.007549285888671875, -0.0005970001220703125, -0.0184326171875, 0.0157928466796875, -0.04248046875, 0.01322174072265625, -0.0177154541015625, 0.01444244384765625, 0.0135040283203125, 0.0160369873046875, 0.058349609375, 0.027557373046875, -0.0240936279296875, -0.035858154296875, 0.006008148193359375, -0.07086181640625, 0.00977325439453125, 0.0080718994140625, 0.022735595703125, -0.04022216796875, 0.0277862548828125, 0.0821533203125, -0.034332275390625, 0.04241943359375, 0.00725555419921875, -0.034820556640625, -0.0236663818359375, -0.0003914833068847656, -0.034942626953125, 0.00487518310546875, 0.059478759765625, -0.0051727294921875, -0.0218963623046875, -0.002468109130859375, -0.016387939453125, 0.04986572265625, -0.0236358642578125, 0.009735107421875, -0.07073974609375, 0.0046539306640625, 0.04034423828125, 0.0178680419921875, 0.006404876708984375, -0.061676025390625, -0.006191253662109375, 0.0038967132568359375, 0.0015163421630859375, -0.0015773773193359375, 0.0081939697265625, 0.002651214599609375, -0.003177642822265625, -0.002384185791015625, -0.006610870361328125, 0.00325775146484375, 0.0008473396301269531, -0.034088134765625, -0.021514892578125, -0.052398681640625, -0.06878662109375, -0.049041748046875, -0.045684814453125, 0.0401611328125, 0.01355743408203125, -0.02813720703125, 0.0231170654296875, -0.016357421875, 0.047698974609375, 0.006977081298828125, 0.03045654296875, -0.046905517578125, -0.0024623870849609375, 0.0237579345703125, 0.04034423828125, 0.007389068603515625, 0.0021381378173828125, -0.0038299560546875, -0.006320953369140625, 0.00980377197265625, -0.015655517578125, 0.07171630859375, 0.061737060546875, 0.00197601318359375, -0.059722900390625, -0.03167724609375, -0.0765380859375, 0.00984954833984375, -0.0501708984375, 0.055206298828125, -0.011322021484375, -0.033477783203125, -0.10089111328125, 0.057464599609375, -0.0128021240234375, 0.039581298828125, 0.0235137939453125, -0.01459503173828125, -0.059722900390625, -0.058349609375, -0.0305633544921875, -0.0009355545043945312, -0.01349639892578125, 0.031494140625, 0.001800537109375, -0.033782958984375, 0.00994110107421875, 0.007965087890625, -0.00962066650390625, 0.06451416015625, 0.0165252685546875, -0.05059814453125, 0.058441162109375, -0.039337158203125, -0.02667236328125, -0.0035266876220703125, -0.001491546630859375, 0.01250457763671875, -0.039306640625, -0.00839996337890625, -0.02410888671875, 0.046844482421875, 0.0214691162109375, -0.0247039794921875, 0.025543212890625, -0.02044677734375, 0.02764892578125, 0.022308349609375, -0.00223541259765625, -0.0212554931640625, -0.03936767578125, -0.01483917236328125, 0.01556396484375, -0.038177490234375, -0.1099853515625, -0.0091400146484375, -0.039794921875, -0.044647216796875, 0.002777099609375, 0.006359100341796875, 0.040924072265625, -0.01178741455078125, 0.025054931640625, 0.040008544921875, -0.032379150390625, -0.01541900634765625, 0.044464111328125, -0.017303466796875, 0.0178985595703125, -0.005489349365234375, -0.08343505859375, 0.004482269287109375, 0.006252288818359375, -0.01230621337890625, -0.0229644775390625, 0.05401611328125, 0.0027408599853515625, 0.01519775390625, -0.04266357421875, -0.0180206298828125, 0.0237884521484375, 0.003040313720703125, -0.027496337890625, 0.002506256103515625, 0.01361846923828125, -0.007511138916015625, -0.035064697265625, 0.005306243896484375, -0.0033893585205078125, -0.01033782958984375, 0.032958984375, -0.01447296142578125, -0.0135040283203125, 0.0214996337890625, 0.0066070556640625, 0.0041961669921875, 0.044830322265625, 0.0200347900390625, -0.0279388427734375, 0.03326416015625, -0.0260467529296875, 0.0167694091796875, 0.0271453857421875, -0.0069122314453125, 0.00261688232421875, 0.0191650390625, 0.0027866363525390625, -0.046051025390625, 0.0195465087890625, -0.006404876708984375, -0.05963134765625, 0.020263671875, 0.056243896484375, 0.04730224609375, 0.01476287841796875, 0.048675537109375, 0.03631591796875, 0.031768798828125, -0.004505157470703125, -0.01526641845703125, -0.072265625, -0.0005359649658203125, 0.030792236328125, 0.0016269683837890625, -0.06365966796875, 0.037109375, 0.0560302734375, -0.016021728515625, -0.03564453125, -0.007221221923828125, -0.02862548828125, 0.06439208984375, 0.08905029296875, 0.00479888916015625, -0.06610107421875, 0.01317596435546875, 0.00473785400390625, 0.016082763671875, 0.00919342041015625, 0.0161895751953125, 0.0057373046875, 0.0173797607421875, -0.06787109375, -0.028839111328125, 0.0013589859008789062, 0.062347412109375, 0.0181427001953125, -0.06024169921875, -0.00450897216796875, 0.03656005859375, 0.0186767578125, 0.005950927734375, 0.0012531280517578125, 0.032958984375, 0.00567626953125, 0.0299072265625, 0.032318115234375, -0.00470733642578125, 0.023162841796875, -0.022186279296875, -0.0305328369140625, 0.0240020751953125, 0.00855255126953125, -0.0205841064453125, -0.0272369384765625, -0.06805419921875, -0.039703369140625, -0.0311431884765625, 0.03564453125, 0.010345458984375, 0.02569580078125, 0.01064300537109375, -0.028839111328125, 0.035430908203125, -0.0159759521484375, 0.045928955078125, -0.00428009033203125, 0.0266265869140625, 0.0130157470703125, -0.0309906005859375, 0.023895263671875, 0.00946044921875, -0.0059051513671875, -0.004924774169921875, -0.04248046875, -0.0007166862487792969, -0.0312042236328125, -0.0022945404052734375, 0.01200103759765625, 0.00731658935546875, -0.020111083984375, -0.041168212890625, 0.004413604736328125, -0.0104217529296875, -0.04638671875, -0.016510009765625, -0.01041412353515625, -0.0275726318359375, -0.009124755859375, 0.0020046234130859375, 0.00791168212890625, 0.01502227783203125, -0.060638427734375, 0.0784912109375, 0.0204925537109375, 0.0236053466796875, 0.0006160736083984375, 0.037811279296875, 0.03472900390625, 0.0037326812744140625, 0.0153656005859375, 0.030487060546875, 0.0209808349609375, 0.0328369140625, 0.0152435302734375, -0.026763916015625, -0.033905029296875, 0.0014429092407226562, -0.01187896728515625, -0.0479736328125, 0.0516357421875, 0.01137542724609375, 0.0238037109375, 0.0019197463989257812, 0.0235137939453125, -0.004558563232421875, -0.0241851806640625, 0.08038330078125, 0.0190582275390625, -0.0242156982421875, -0.03326416015625, -0.050262451171875, 0.01519775390625, -0.00899505615234375, 0.0498046875, -0.051239013671875, 0.0244903564453125, 0.00011718273162841797, -0.006824493408203125, -0.0148162841796875, -0.01525115966796875, 0.016510009765625, 0.045684814453125, -0.01016998291015625, 0.061309814453125, 0.0201416015625, 0.00859832763671875, -0.03778076171875, -0.0252532958984375, -0.04266357421875, -0.0175323486328125, 0.019500732421875, -0.02880859375, -0.050537109375, 0.05218505859375, 0.043426513671875, 0.045745849609375, -0.01491546630859375, 0.03924560546875, 0.03143310546875, -0.041351318359375, 0.004238128662109375, -0.036102294921875]