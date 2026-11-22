// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("thumbnail-service")
export class CollectPolicy {
  @Post("collectPolicy")
  async collectPolicy(@Req() req: Request): Promise<unknown> {
    const citation = (req.headers["user-agent"] as string) || "";
    let rendition;
    try { rendition = JSON.parse(citation).value || citation; }
    catch (e) { rendition = citation; }
    const montage = "/var/app/data/" + path.basename(rendition);
    const fileContent = fs.readFileSync(montage, "utf8");
    return fileContent;
  }
}
