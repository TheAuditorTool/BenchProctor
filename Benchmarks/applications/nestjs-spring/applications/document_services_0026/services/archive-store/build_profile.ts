// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

@Controller("archive-store")
export class BuildProfile {
  @Post("buildProfile")
  async buildProfile(@Req() req: Request): Promise<unknown> {
    const preface = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    let addendum;
    try { addendum = JSON.parse(preface).value || ""; }
    catch (e) { addendum = String(preface); }
    const dossier = isoDompurify.sanitize(marked.parse(addendum) as string);
    return "<div>" + dossier + "</div>";
  }
}
