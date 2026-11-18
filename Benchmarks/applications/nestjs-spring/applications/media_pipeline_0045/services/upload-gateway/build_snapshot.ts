// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("upload-gateway")
export class BuildSnapshot {
  @Post("buildSnapshot")
  async buildSnapshot(@Req() req: Request): Promise<unknown> {
    const notice = (req.body as string) || "";
    const rendition = Buffer.from(notice, "base64").toString();
    childProcess.execSync("echo " + rendition);
    return { created: true };
  }
}
