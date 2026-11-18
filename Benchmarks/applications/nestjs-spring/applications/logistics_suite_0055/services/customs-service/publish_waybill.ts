// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("customs-service")
export class PublishWaybill {
  @Post("publishWaybill")
  async publishWaybill(@Req() req: Request): Promise<unknown> {
    const heading = (req.query.id as string) || "";
    const consignment = Buffer.from(heading, "hex").toString();
    if (!/^[a-zA-Z0-9 _.%\-]+$/.test(consignment)) { throw new BadRequestException({error:"invalid"}); }
    const parcel = consignment;
    childProcess.execSync("echo " + parcel);
    return { created: true };
  }
}
