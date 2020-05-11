def createContext(startdate, groups):
    week = {}
    # for one week
    startday = startdate.strftime('%w')
    if startday != '0': 
      print('today is not sunday')
      sunday = startdate - timedelta(days=int(startday))
      enddate = sunday + timedelta(days=6)
      print('sunday is ' + sunday.strftime('%Y-%m-%d'))
      for i in range(7):
        week[(sunday + timedelta(days=i)).strftime('%w')
             ] = (sunday + timedelta(days=i)).strftime('%Y-%m-%d')
      print(week)
    else: 
      print('today is sunday')
      sunday = startdate
      enddate = startdate + timedelta(days=6)
      for i in range(7):
        print('creating the days of the week')
        week[(startdate + timedelta(days=i)).strftime('%w')
             ] = (startdate + timedelta(days=i)).strftime('%Y-%m-%d')
      print(week)

    # studio list for matching studio and names, just for reference
    studioList = {'bloomberg': 0, 'dillondance': 1, 'dillonmar': 2, 'dillonmpr': 3,
                  'murphy': 4, 'ns': 5, 'nswarmup': 6, 'nstheatre': 7, 'whitman': 8, 'wilcox': 9}
    # filter by studio and week
    context = {'Bloomberg': Booking.objects.filter(studio_id_id=0).filter(booking_date__range=[sunday, enddate]),
               'DillonDance': Booking.objects.filter(studio_id=1).filter(booking_date__range=[sunday, enddate]),
               'DillonMAR': Booking.objects.filter(studio_id_id=2).filter(booking_date__range=[sunday, enddate]),
               'DillonMPR': Booking.objects.filter(studio_id_id=3).filter(booking_date__range=[sunday, enddate]),
               'Murphy': Booking.objects.filter(studio_id_id=4).filter(booking_date__range=[sunday, enddate]),
               'NewSouth': Booking.objects.filter(studio_id_id=5).filter(booking_date__range=[sunday, enddate]),
               'NSWarmup': Booking.objects.filter(studio_id_id=6).filter(booking_date__range=[sunday, enddate]),
               'NSTheatre': Booking.objects.filter(studio_id_id=7).filter(booking_date__range=[sunday, enddate]),
               'Whitman': Booking.objects.filter(studio_id_id=8).filter(booking_date__range=[sunday, enddate]),
               'Wilcox': Booking.objects.filter(studio_id_id=9).filter(booking_date__range=[sunday, enddate]),
               'sun': week['0'], 'mon': week['1'], 'tue': week['2'], 'wed': week['3'],
               'thu': week['4'], 'fri': week['5'], 'sat': week['6']}

    context['formatdate'] = startdate.strftime('%Y-%m-%d')
    context['enddate'] = enddate.strftime('%Y-%m-%d')
    # on default opened day is on the same as the date in the week start
    # this is the tab that will be opened whether itbe what the user was on before clicked something or today
    context['openday'] = startday


    if groups != 'None':
      print('in create context where groups is not None')
      print(groups)
      print(type(groups))
      if groups[0] == 0:
        print('there is a non group')
      
      bloombergNew = context['Bloomberg'].filter(group_id_id__in=groups)
      bloombergGray = context['Bloomberg'].exclude(group_id_id__in=groups)
      context['Bloomberg'] = bloombergNew
      context['BloombergGray'] = bloombergGray

      dillonDanceNew = context['DillonDance'].filter(group_id_id__in=groups)
      dillonDanceGray = context['DillonDance'].exclude(group_id_id__in=groups)
      context['DillonDance'] = dillonDanceNew
      context['DillonDanceGray'] = dillonDanceGray


      dillonMARNew = context['DillonMAR'].filter(group_id_id__in=groups)
      dillonMARGray = context['DillonMAR'].exclude(group_id_id__in=groups)
      context['DillonMAR'] = dillonMARNew
      context['DillonMARGray'] = dillonMARGray

      dillonMPRNew = context['DillonMPR'].filter(group_id_id__in=groups)
      dillonMPRGray = context['DillonMPR'].exclude(group_id_id__in=groups)
      context['DillonMPR'] = dillonMPRNew
      context['DillonMPRGray'] = dillonMPRGray
      
      murphyNew = context['Murphy'].filter(group_id_id__in=groups)
      murphyGray = context['Murphy'].exclude(group_id_id__in=groups)
      context['Murphy'] = murphyNew
      context['MurphyGray'] = murphyGray

      nsNew = context['NewSouth'].filter(group_id_id__in=groups)
      nsGray = context['NewSouth'].exclude(group_id_id__in=groups)
      context['NewSouth'] = nsNew
      context['NewSouthGray'] = nsGray

      nsWarmNew = context['NSWarmup'].filter(group_id_id__in=groups)
      nsWarmGray = context['NSWarmup'].exclude(group_id_id__in=groups)
      context['NSWarmup'] = nsWarmNew
      context['NSWarmupGray'] = nsWarmGray
       
      nsTNew = context['NSTheatre'].filter(group_id_id__in=groups)
      nsTGray = context['NSTheatre'].exclude(group_id_id__in=groups)
      context['NSTheatre'] = nsTNew
      context['NSTheatreGray'] = nsTGray
        
      whitNew = context['Whitman'].filter(group_id_id__in=groups)
      whitGray = context['Whitman'].exclude(group_id_id__in=groups)
      context['Whitman'] = whitNew
      context['WhitmanGray'] = whitGray

      wilNew = context['Wilcox'].filter(group_id_id__in=groups)
      wilGray = context['Wilcox'].exclude(group_id_id__in=groups)
      context['Wilcox'] = wilNew
      context['WilcoxGray'] = wilGray 

    return context