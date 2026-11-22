// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("metrics-ingest")
export class ValidateAlert {
  @Post("validateAlert")
  async validateAlert(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.headers["user-agent"] as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(excerpt);
    const cohort: string = readInput();
    childProcess.execSync("echo " + cohort);
    return { created: true };
  }
}
