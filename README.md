# obspyDMT: A Python Toolbox for Retrieving and Processing of Large Seismological Datasets

Welcome to obspyDMT version 2.0.0 tutorial!

obspyDMT_ (obspy Data Management Tool) is a command line tool for retrieving, processing and management of large seismological datasets in a fully automatic way which can be run in serial or in parallel.

Software functionality:

-   Query of station meta-data: by absolute time or relative to earthquake occurrences; by geographic area (rectangles or circles); by channel or instrument type; wildcarding (\*) is supported; simultaneous queries of different data centers.

-   Query of earthquake source meta-data: from different catalogue providers (NEIC, Global CMT, IRIS DMC, NERIES, NCEDC, USGS, INGV and ISC); event origin information or full moment tensors; by time window, region, event magnitude and/or event depth.

-   Diagnostic plots to visualize meta-data; plots are generated by simple inclusion of an option flag.

-   Retrieval of actual waveform data (seismograms) according to the results of meta-data queries. Support for different protocols (FDSN web services, ArcLink).

-   Retrieval of time-continuous series of arbitrary length; diagnostic log files.

-   Parallelized retrieval of waveform data for increased speed. Simultaneous retrieval from different data centers.

-   Update mode: identical or modified queries can be relaunched; only new, modified, or previously failed data will be retrieved from the data center(s).

-   Tolerant of retrieval errors and missing data (includes diagnostic logs).

-   Automatic organisation of data, meta-data and log files into standardized directory trees. (At present no tie to any specific database system.)

-   Processing of the data set using default or user-defined processing function; user can customize the processing unit by writing a script in obspy, SAC and/or any other processing tool on the waveform level; Application to the whole data set directly after data-retrieval or as a separate step. Support for parallelized processing. 

-   Application of instrument responses. Support for various instrument formats (StationXML, Dataless SEED). Diagnostic plots of analog and digital filter stages. Option of parallelized instrument correction, taking advantage of multicore architectures even on desktop processors.

-   Retrieval of synthetic seismograms, for comparison to real data.



This tutorial has been divided into the following sections: 

1.  [How to cite obspyDMT]()
2.  `Lets get started`_: install obspyDMT and check your local machine for required dependencies.
3.  `Quick tour`_: run a quick tour.
4.  `Option types`_: there are two types of options in obspyDMT: *option-1* (with value) and *option-2* (without value)
5.  `event-info request`_: if you are looking for some events and you want to get info about them without downloading waveforms.
6.  `event-based request`_: retrieve the waveforms, stationXML/response files and meta-data of all the requested stations for all the events found in the archive.
7.  `continuous request`_: retrieve the waveforms, stationXML/response files and meta-data of all the requested stations and for the requested time span.
8.  `Update`_: if you want to continue an interrupted request or complete your existing archive.
9.  `Geographical restriction`_: if you want to work with the events happened in a specific geographical coordinate and/or retrieving the data from the stations in a specific circular or rectangular bounding area.
10. `Instrument correction`_: applying instrument correction to raw counts using stationXML/response files.
11. `Parallel retrieving and processing`_: send the requests and/or process the data in parallel. This section introduces some options (*bulk* and *parallel retrieving and processing*) to speed-up the whole procedure.
12. `Resampling raw and corrected waveforms`_: how to automatically resample raw and/or corrected waveforms while creating a database.
13. `Plot`_: for an existing archive, you can plot all the events and/or all the stations, ray path for event-station pairs and epicentral-distance/time for the waveforms using GMT-5 or basemap tools.
14. `Explore stationXML file`_: how to explore and analyze different stages available in a stationXML file.
15. `Seismicity`_: plot the geographical and historical distribution of earthquake activities (seismicity).
16. `NEIC and GCMT`_: retrieving event information including moment tensor from NEIC or GCMT.
17. `Folder structure`_: the way that obspyDMT organizes your retrieved and processed data in the file-based mode.
18. `Available options`_: all options currently available in obspyDMT.
19. `Algorithm`_: flow chart of the main steps in each obspyDMT mode.
20. `Example: RHUM-RUM stations`_: exclusively for RHUM-RUM users.

## How to cite obspyDMT

If you use obspyDMT, please consider citing the code as:

```
Kasra Hosseini (2015), obspyDMT (Version 1.0.0) [software] [https://github.com/kasra-hosseini/obspyDMT]
```

We have also published a paper in SRL (Seismological Research Letters) for obspyDMT's predecessor that we kindly ask you to cite in case that you found obspyDMT useful for your research:

```
C. Scheingraber, K. Hosseini, R. Barsch, and K. Sigloch (2013), ObsPyLoad - a tool for fully automated retrieval of seismological waveform data, Seismological Research Letters, 84(3), 525-531, DOI:10.1785/0220120103.
```
