// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("carrier-gateway")
export class ArchiveRoster {
  @Post("archiveRoster")
  async archiveRoster(@Req() req: Request): Promise<unknown> {
    const citation = (req.cookies?.session_token as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const parcel: string = normalize(citation);
    if (!/^(asc|desc|name|created)$/.test(String(parcel))) { throw new BadRequestException({error:"invalid"}); }
    const consignment = parcel;
    fs.unlinkSync("/var/app/data/" + consignment);
    return { created: true };
  }
}
