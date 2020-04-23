--Drop Tables--
drop table dow_usa;
drop table covid_usa;

--Create Tables--
create table dow_usa(
	time VARCHAR,
	open VARCHAR,
	high VARCHAR,
	low VARCHAR,
	last VARCHAR,
	change VARCHAR,
	volume VARCHAR);

create table covid_usa(
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
select * from dow_usa;
select * from covid_usa;

--Combine on Date--
create view usa_combined as 
select dow_usa.time,
		dow_usa.open,
		dow_usa.high,
		dow_usa.low,
		dow_usa.last,
		dow_usa.change,
		dow_usa.volume,
		covid_usa.cases,
		covid_usa.deaths,
		covid_usa.geoid
from dow_usa
inner join covid_usa on
dow_usa.time = covid_usa.daterep;

select * from usa_combined;