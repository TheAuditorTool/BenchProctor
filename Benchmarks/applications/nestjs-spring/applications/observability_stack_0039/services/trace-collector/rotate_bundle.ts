// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("trace-collector")
export class RotateBundle {
  @Post("rotateBundle")
  async rotateBundle(@Req() req: Request): Promise<unknown> {
    const caption = (req.headers.referer as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(caption);
    const cohort: string = readInput();
    fs.writeFileSync("/var/uploads/" + cohort, "data");
    return { created: true };
  }
}
