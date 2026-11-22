// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("index-builder")
export class BuildRoster {
  @Post("buildRoster")
  async buildRoster(@Req() req: Request): Promise<unknown> {
    const snippet = (req.headers["user-agent"] as string) || "";
    let addendum;
    try { addendum = JSON.parse(snippet).value || snippet; }
    catch (e) { addendum = snippet; }
    const dossier = "/var/app/data/" + path.basename(addendum);
    const fileContent = fs.readFileSync(dossier, "utf8");
    return fileContent;
  }
}
