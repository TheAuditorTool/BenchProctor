// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("trace-collector")
export class CollectMetric {
  @Post("collectMetric")
  async collectMetric(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.headers["user-agent"] as string) || "";
    let gauge;
    try { gauge = JSON.parse(paragraph).value || paragraph; }
    catch (e) { gauge = paragraph; }
    const cohort = "/var/app/data/" + path.basename(gauge);
    const fileContent = fs.readFileSync(cohort, "utf8");
    return fileContent;
  }
}
