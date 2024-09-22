/*---------------------------------------------------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     |
    \\  /    A nd           | www.openfoam.com
     \\/     M anipulation  |
-------------------------------------------------------------------------------
    Copyright (C) 2019-2021 OpenCFD Ltd.
    Copyright (C) YEAR AUTHOR, AFFILIATION
-------------------------------------------------------------------------------
License
    This file is part of OpenFOAM.

    OpenFOAM is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    OpenFOAM is distributed in the hope that it will be useful, but WITHOUT
    ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
    FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
    for more details.

    You should have received a copy of the GNU General Public License
    along with OpenFOAM.  If not, see <http://www.gnu.org/licenses/>.

\*---------------------------------------------------------------------------*/

#include "functionObjectTemplate.H"
#define namespaceFoam  // Suppress <using namespace Foam;>
#include "fvCFD.H"
#include "unitConversion.H"
#include "addToRunTimeSelectionTable.H"

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

namespace Foam
{

// * * * * * * * * * * * * * * Static Data Members * * * * * * * * * * * * * //

defineTypeNameAndDebug(diffFunctionObject, 0);

addRemovableToRunTimeSelectionTable
(
    functionObject,
    diffFunctionObject,
    dictionary
);


// * * * * * * * * * * * * * * * Global Functions  * * * * * * * * * * * * * //

// dynamicCode:
// SHA1 = d924c92ec3fe0b16fec6b8892a9fc1c20fa93dd8
//
// unique function name that can be checked if the correct library version
// has been loaded
extern "C" void diff_d924c92ec3fe0b16fec6b8892a9fc1c20fa93dd8(bool load)
{
    if (load)
    {
        // Code that can be explicitly executed after loading
    }
    else
    {
        // Code that can be explicitly executed before unloading
    }
}


// * * * * * * * * * * * * * * * Local Functions * * * * * * * * * * * * * * //

//{{{ begin localCode

//}}} end localCode

} // End namespace Foam


// * * * * * * * * * * * * * Private Member Functions  * * * * * * * * * * * //

const Foam::fvMesh&
Foam::diffFunctionObject::mesh() const
{
    return refCast<const fvMesh>(obr_);
}


// * * * * * * * * * * * * * * * * Constructors  * * * * * * * * * * * * * * //

Foam::
diffFunctionObject::
diffFunctionObject
(
    const word& name,
    const Time& runTime,
    const dictionary& dict
)
:
    functionObjects::regionFunctionObject(name, runTime, dict)
{
    read(dict);
}


// * * * * * * * * * * * * * * * * Destructor  * * * * * * * * * * * * * * * //

Foam::
diffFunctionObject::
~diffFunctionObject()
{}


// * * * * * * * * * * * * * * * Member Functions  * * * * * * * * * * * * * //

bool
Foam::
diffFunctionObject::read(const dictionary& dict)
{
    if (false)
    {
        printMessage("read diff");
    }

//{{{ begin code
    
//}}} end code

    return true;
}


bool
Foam::
diffFunctionObject::execute()
{
    if (false)
    {
        printMessage("execute diff");
    }

//{{{ begin code
    
//}}} end code

    return true;
}


bool
Foam::
diffFunctionObject::write()
{
    if (false)
    {
        printMessage("write diff");
    }

//{{{ begin code
    #line 56 "/home/hakan/courses/testSimulation/tgv2dTests/tgv2d_temporal/RK4Foam/RK4Foam_nu1/TGV_temporal/system/controlDict/functions/diff"
const volVectorField& c = mesh().C();
			const volScalarField x = c & vector(1.0, 0.0, 0.0);
			const volScalarField y = c & vector(0.0, 1.0, 0.0);
			const Time& time_ = mesh().time();
			const volVectorField& U = mesh().lookupObject<volVectorField>("U");
			const volScalarField& p = mesh().lookupObject<volScalarField>("p");

			scalarField p_a(mesh().nCells(), 0.0);
			
			volVectorField analytical_velocity
			(
				IOobject
				(
					"analytical_velocity",
					time().timeName(),
					mesh(),
					IOobject::READ_IF_PRESENT,
					IOobject::AUTO_WRITE
				),
				mesh(),
				dimensionedVector(dimVelocity, Zero)
			);

			volVectorField error_velocity
			(
				IOobject
				(
					"error_velocity",
					time().timeName(),
					mesh(),
					IOobject::READ_IF_PRESENT,
					IOobject::AUTO_WRITE
				),
				mesh(),
				dimensionedVector(dimVelocity, Zero)
			);
			volScalarField error_velocity_mag
			(
				IOobject
				(
					"error_velocity_mag",
					time().timeName(),
					mesh(),
					IOobject::READ_IF_PRESENT,
					IOobject::AUTO_WRITE
				),
				mesh(),
				dimensionedScalar(dimVelocity*dimVelocity, Zero)
			);

			volScalarField error_velocity_mag_squ
			(
				IOobject
				(
					"error_velocity_mag_squ",
					time().timeName(),
					mesh(),
					IOobject::READ_IF_PRESENT,
					IOobject::AUTO_WRITE
				),
				mesh(),
				dimensionedScalar(dimVelocity*dimVelocity, Zero)
			);
			volScalarField analytical_pres
			(
				IOobject
				(
					"analytical_pres",
					time().timeName(),
					mesh(),
					IOobject::READ_IF_PRESENT,
					IOobject::AUTO_WRITE
				),
				mesh(),
				dimensionedScalar(dimPressure, Zero)
			);
			volScalarField error_pres
			(
				IOobject
				(
					"error_pres",
					time().timeName(),
					mesh(),
					IOobject::READ_IF_PRESENT,
					IOobject::AUTO_WRITE
				),
				mesh(),
				dimensionedScalar(dimPressure, Zero)
			);

			const scalar k = 1.0;
			//const scalar nu = 1.0;
			//connected to nu in controlDict, which is used for the analytical solution, change one, change the other as well.
			
			IOdictionary transportProperties
			(
			 IOobject
			 (
			  "transportProperties",
			  time().constant(),
			  mesh(),
			  IOobject::MUST_READ_IF_MODIFIED,
			  IOobject::NO_WRITE
			 )
			);

			const auto nu = transportProperties.get<scalar>("nu");

			const scalar rho = 1.0;
			forAll(c, i){
				scalar vx, vy, vz;
				vx = -Foam::cos(k*x[i])*Foam::sin(k*y[i])*std::exp(-2.*nu*std::pow(k,2.)*time_.value());
				vy =  Foam::sin(k*x[i])*Foam::cos(k*y[i])*std::exp(-2.*nu*std::pow(k,2.)*time_.value());
				vz = 0.0;

				analytical_velocity[i] = vector(vx, vy, vz);
				error_velocity[i] = analytical_velocity[i] - U[i];
				error_velocity_mag[i] = mag(error_velocity[i]);
				error_velocity_mag_squ[i] = std::pow(error_velocity_mag[i],2.0);
				analytical_pres[i] = -0.25*(Foam::cos(2.*k*x[i]) + Foam::cos(2.*k*y[i]))*std::exp(-4.*nu*std::pow(k,2.)*time_.value());
				error_pres[i] = mag(analytical_pres[i] - p[i]);

			}
			analytical_velocity.write();
			error_velocity.write();
			error_velocity_mag.write();
			error_velocity_mag_squ.write();
			analytical_pres.write();
			error_pres.write();
//}}} end code

    return true;
}


bool
Foam::
diffFunctionObject::end()
{
    if (false)
    {
        printMessage("end diff");
    }

//{{{ begin code
    
//}}} end code

    return true;
}


// ************************************************************************* //

