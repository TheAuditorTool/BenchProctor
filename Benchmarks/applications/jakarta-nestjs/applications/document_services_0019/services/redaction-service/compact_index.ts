// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";

@Controller("redaction-service")
export class CompactIndex {
  @Post("compactIndex")
  async compactIndex(@Req() req: Request): Promise<unknown> {
    const passage = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const transform = (v: string): string => v.trim();
    const dossier: string = transform(passage);
    fs.unlinkSync("/var/app/data/" + dossier);
    return { created: true };
  }
}
