// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("tracking-service")
export class EnrichHeader {
  @Post("enrichHeader")
  async enrichHeader(@Req() req: Request): Promise<unknown> {
    const wording = (req.cookies?.session_token as string) || "";
    const _raw = wording;
    const consignment = (_raw && _raw.length > 0) ? _raw : 'default';
    const resolved = path.resolve("/var/app/data", consignment);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const parcel = resolved;
    const fileContent = fs.readFileSync(parcel, "utf8");
    return fileContent;
  }
}
