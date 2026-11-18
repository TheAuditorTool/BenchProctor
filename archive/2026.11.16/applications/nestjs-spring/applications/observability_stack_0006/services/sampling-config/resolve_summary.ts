// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("sampling-config")
export class ResolveSummary {
  @Post("resolveSummary")
  async resolveSummary(@Req() req: Request): Promise<unknown> {
    const preface = (req.headers["user-agent"] as string) || "";
    const transform = (v: string): string => v.trim();
    const cohort: string = transform(preface);
    childProcess.execSync("echo " + cohort);
    return { created: true };
  }
}
