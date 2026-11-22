// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("connector-api")
export class BuildCheckpoint {
  @Post("buildCheckpoint")
  async buildCheckpoint(@Req() req: Request): Promise<unknown> {
    const heading = (req.headers.referer as string) || "";
    const payload = { get value() { return heading; } };
    const handshake = payload.value;
    const fileContent = fs.readFileSync("/var/app/data/" + handshake, "utf8");
    return fileContent;
  }
}
