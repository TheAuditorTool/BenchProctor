// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

@Controller("metrics-ingest")
export class RotateDigest {
  @Post("rotateDigest")
  async rotateDigest(@Req() req: Request): Promise<unknown> {
    const note = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    let cohort;
    try { cohort = JSON.parse(note).value || ""; }
    catch (e) { cohort = String(note); }
    const gauge = isoDompurify.sanitize(marked.parse(cohort) as string);
    return "<div>" + gauge + "</div>";
  }
}
