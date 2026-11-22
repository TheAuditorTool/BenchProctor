// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("decision-log")
export class FormatBatch {
  @Post("formatBatch/:id")
  async formatBatch(@Req() req: Request): Promise<unknown> {
    const memo = (req.params.id as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const verdict: string = normalize(memo);
    const fileContent = fs.readFileSync("/var/app/data/" + verdict, "utf8");
    return fileContent;
  }
}
