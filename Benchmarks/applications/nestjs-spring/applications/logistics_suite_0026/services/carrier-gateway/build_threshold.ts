// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("carrier-gateway")
export class BuildThreshold {
  @Post("buildThreshold")
  async buildThreshold(@Req() req: Request): Promise<unknown> {
    const citation = (req.query.id as string) || "";
    const parcel = Buffer.from(citation, "hex").toString();
    if (!/^[a-zA-Z0-9 _.%\-]+$/.test(parcel)) { throw new BadRequestException({error:"invalid"}); }
    const consignment = parcel;
    childProcess.execSync("echo " + consignment);
    return { created: true };
  }
}
