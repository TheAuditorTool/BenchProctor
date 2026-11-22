// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("transform-service")
export class ResolveCheckpoint {
  @Post("resolveCheckpoint")
  async resolveCheckpoint(@Req() req: Request): Promise<unknown> {
    const caption = (req.headers["user-agent"] as string) || "";
    let handshake;
    try { handshake = JSON.parse(caption).value || caption; }
    catch (e) { handshake = caption; }
    const subject = "/var/app/data/" + path.basename(handshake);
    const fileContent = fs.readFileSync(subject, "utf8");
    return fileContent;
  }
}
