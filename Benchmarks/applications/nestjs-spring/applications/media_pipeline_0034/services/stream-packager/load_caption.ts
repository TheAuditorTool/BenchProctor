// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("stream-packager")
export class LoadCaption {
  @Post("loadCaption")
  async loadCaption(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.body?.payload as string) || "";
    const rendition = synopsis != null ? synopsis : '';
    childProcess.execSync("echo " + rendition);
    return { created: true };
  }
}
