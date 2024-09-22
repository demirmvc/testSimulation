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
#line 23 "/home/hakan/courses/testSimulation/tgv2dTests/tgv2d_temporal/RK4Foam/RK4Foam_nu1/TGV_temporal/0/p/#codeStream"
#include "fvCFD.H"
//}}} end codeInclude

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

namespace Foam
{

// * * * * * * * * * * * * * * * Local Functions * * * * * * * * * * * * * * //

//{{{ begin localCode

//}}} end localCode


// * * * * * * * * * * * * * * * Global Functions  * * * * * * * * * * * * * //

extern "C" void codeStream_537564b8bd232f4ddf4797bc6f60eef024868c2e(Foam::Ostream& os, const Foam::dictionary& dict)
{
//{{{ begin code
    #line 40 "/home/hakan/courses/testSimulation/tgv2dTests/tgv2d_temporal/RK4Foam/RK4Foam_nu1/TGV_temporal/0/p/#codeStream"
const IOdictionary& d = static_cast<const IOdictionary&>(dict);
		const fvMesh& mesh = refCast<const fvMesh>(d.db());

		scalarField init_p(mesh.nCells(), 0.0);
	    
		forAll(init_p, i)
		{
			const scalar x = mesh.C()[i][0];
			const scalar y = mesh.C()[i][1];

		init_p[i] = -0.25*(Foam::cos(2.*x) + Foam::cos(2.*y));
		}

		init_p.writeEntry("", os);
//}}} end code
}


// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

} // End namespace Foam

// ************************************************************************* //

