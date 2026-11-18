// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("rate-shopper")
export class ArchiveSnapshot {
  @Post("archiveSnapshot")
  async archiveSnapshot(@Req() req: Request): Promise<unknown> {
    const caption = (req.body?.variables?.input as string) || "";
    const payload = { get value() { return caption; } };
    const parcel = payload.value;
    if (!/^(asc|desc|name|created)$/.test(String(parcel))) { throw new BadRequestException({error:"invalid"}); }
    const consignment = parcel;
    const fileContent = fs.readFileSync("/var/app/data/" + consignment, "utf8");
    return fileContent;
  }
}
