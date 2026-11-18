// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";
import * as path from "path";

@Controller("thumbnail-service")
export class RotateIndex {
  @Post("rotateIndex")
  async rotateIndex(@Req() req: Request): Promise<unknown> {
    const passage = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    const transform = (v: string): string => v.trim();
    const montage: string = transform(passage);
    const resolved = path.resolve("/var/app/data", montage);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const rendition = resolved;
    const fileContent = fs.readFileSync(rendition, "utf8");
    return fileContent;
  }
}
