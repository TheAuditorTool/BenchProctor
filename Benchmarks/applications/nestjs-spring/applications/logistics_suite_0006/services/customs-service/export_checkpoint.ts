// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("customs-service")
export class ExportCheckpoint {
  @Post("exportCheckpoint")
  async exportCheckpoint(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers["x-forwarded-for"] as string) || "";
    const consignment = summary != null ? summary : '';
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(consignment)) { throw new BadRequestException({error:"invalid"}); }
    const parcel = consignment;
    return "<div>" + parcel + "</div>";
  }
}
