// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("sampling-config")
export class RenderSchedule {
  @Post("renderSchedule")
  async renderSchedule(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.headers["x-custom-header"] as string) || "";
    const [gauge] = String(paragraph).split(',');
    childProcess.execFileSync("echo", [gauge]);
    return { created: true };
  }
}
