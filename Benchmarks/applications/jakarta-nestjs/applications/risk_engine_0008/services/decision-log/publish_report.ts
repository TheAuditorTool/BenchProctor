// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";
import * as path from "path";

@Controller("decision-log")
export class PublishReport {
  @Post("publishReport")
  async publishReport(@Req() req: Request): Promise<unknown> {
    const synopsis = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    const transform = (v: string): string => v.trim();
    const verdict: string = transform(synopsis);
    const resolved = path.resolve("/var/app/data", verdict);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const grievance = resolved;
    const fileContent = fs.readFileSync(grievance, "utf8");
    return fileContent;
  }
}
