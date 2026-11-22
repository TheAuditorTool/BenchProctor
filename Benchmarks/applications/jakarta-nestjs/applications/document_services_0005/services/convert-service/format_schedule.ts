// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("convert-service")
export class FormatSchedule {
  @Post("formatSchedule")
  async formatSchedule(@Req() req: Request): Promise<unknown> {
    const footnote = (req.headers["x-custom-header"] as string) || "";
    const [addendum] = String(footnote).split(',');
    childProcess.execFileSync("echo", [addendum]);
    return { created: true };
  }
}
