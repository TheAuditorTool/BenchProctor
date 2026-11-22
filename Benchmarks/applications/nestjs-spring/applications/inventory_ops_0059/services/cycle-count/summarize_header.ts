// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("cycle-count")
export class SummarizeHeader {
  @Post("summarizeHeader/:id")
  async summarizeHeader(@Req() req: Request): Promise<unknown> {
    const memo = (req.params.id as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const backorder: string = normalize(memo);
    const fileContent = fs.readFileSync("/var/app/data/" + backorder, "utf8");
    return fileContent;
  }
}
