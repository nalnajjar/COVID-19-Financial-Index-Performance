--Drop Tables--
drop table kospi_korea;
drop table covid_korea;

--Create Tables--
create table kospi_korea(
	time VARCHAR,
	open VARCHAR,
	high VARCHAR,
	low VARCHAR,
	last VARCHAR,
	change VARCHAR,
	volume VARCHAR);

create table covid_korea(
	daterep VARCHAR,
	day VARCHAR,
	month VARCHAR,
	year VARCHAR,
	cases INT,
	deaths INT,
	countries_and_territories VARCHAR,
	GeoId VARCHAR,
    countryterritorycode VARCHAR,
	popdata2018 INT);
	
--Check Data--
select * from kospi_korea;
select * from covid_korea;

--Combine on Date--
create view korea_combined as 
select kospi_korea.time,
		kospi_korea.open,
		kospi_korea.high,
		kospi_korea.low,
		kospi_korea.last,
		kospi_korea.change,
		kospi_korea.volume,
		covid_korea.cases,
		covid_korea.deaths,
		covid_korea.geoid
from kospi_korea
inner join covid_korea on
kospi_korea.time = covid_korea.daterep;

select * from korea_combined;