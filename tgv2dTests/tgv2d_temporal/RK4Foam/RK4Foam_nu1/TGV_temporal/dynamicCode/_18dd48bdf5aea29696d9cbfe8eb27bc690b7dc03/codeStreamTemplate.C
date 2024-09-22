/*---------------------------------------------------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     |
    \\  /    A nd           | www.openfoam.com
     \\/     M anipulation  |
-------------------------------------------------------------------------------
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

Description
    Template for use with codeStream.

\*---------------------------------------------------------------------------*/

#include "dictionary.H"
#include "Ostream.H"
#include "Pstream.H"
#include "pointField.H"
#include "tensor.H"
#include "unitConversion.H"

//{{{ begin codeInclude
#line 23 "/home/hakan/courses/testSimulation/tgv2dTests/tgv2d_temporal/RK4Foam/RK4Foam_nu1/TGV_temporal/0/U/#codeStream"
#include "fvCFD.H"
//}}} end codeInclude

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

namespace Foam
{

// * * * * * * * * * * * * * * * Local Functions * * * * * * * * * * * * * * //

//{{{ begin localCode

//}}} end localCode


// * * * * * * * * * * * * * * * Global Functions  * * * * * * * * * * * * * //

extern "C" void codeStream_18dd48bdf5aea29696d9cbfe8eb27bc690b7dc03(Foam::Ostream& os, const Foam::dictionary& dict)
{
//{{{ begin code
    #line 40 "/home/hakan/courses/testSimulation/tgv2dTests/tgv2d_temporal/RK4Foam/RK4Foam_nu1/TGV_temporal/0/U/#codeStream"
const IOdictionary& d = static_cast<const IOdictionary&>(dict);
		const fvMesh& mesh = refCast<const fvMesh>(d.db());

		vectorField init_U(mesh.nCells(), vector(0.0, 0.0, 0.0));
	    
		forAll(init_U, i)
		{
			const scalar x = mesh.C()[i][0];
			const scalar y = mesh.C()[i][1];

			const scalar u = -Foam::cos(x)*Foam::sin(y);
			const scalar v =  Foam::sin(x)*Foam::cos(y);

			init_U[i] = vector(u, v, 0.0);
		}

		init_U.writeEntry("", os);
//}}} end code
}


// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

} // End namespace Foam

// ************************************************************************* //

