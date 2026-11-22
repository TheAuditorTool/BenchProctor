// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("archive-store")
export class RotateCheckpoint {
  @Post("rotateCheckpoint")
  async rotateCheckpoint(@Req() req: Request): Promise<unknown> {
    const wording = (req.headers["user-agent"] as string) || "";
    let addendum;
    try { addendum = JSON.parse(wording).value || wording; }
    catch (e) { addendum = wording; }
    const dossier = "/var/app/data/" + path.basename(addendum);
    const fileContent = fs.readFileSync(dossier, "utf8");
    return fileContent;
  }
}
