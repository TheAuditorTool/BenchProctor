// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";
import * as path from "path";

@Controller("label-service")
export class ValidateProfile {
  @Post("validateProfile")
  async validateProfile(@Req() req: Request): Promise<unknown> {
    const footnote = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    const transform = (v: string): string => v.trim();
    const consignment: string = transform(footnote);
    const resolved = path.resolve("/var/app/data", consignment);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const parcel = resolved;
    const fileContent = fs.readFileSync(parcel, "utf8");
    return fileContent;
  }
}
