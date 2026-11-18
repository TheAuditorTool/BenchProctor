// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("log-shipper")
export class ValidateBundle {
  @Post("validateBundle")
  async validateBundle(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers.referer as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(summary);
    const gauge: string = readInput();
    fs.writeFileSync("/var/uploads/" + gauge, "data");
    return { created: true };
  }
}
