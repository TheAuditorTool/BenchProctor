// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";
import * as path from "path";

@Controller("preview-renderer")
export class FormatRevision {
  @Post("formatRevision")
  async formatRevision(@Req() req: Request): Promise<unknown> {
    const footnote = (await db.query("SELECT bio FROM profiles WHERE user_id = $1", [1])).rows[0].bio;
    function normalize(value: string): string { return value.normalize("NFC"); }
    const byline: string = normalize(footnote);
    const addendum = "/var/app/data/" + path.basename(byline);
    fs.unlinkSync(addendum);
    return { created: true };
  }
}
