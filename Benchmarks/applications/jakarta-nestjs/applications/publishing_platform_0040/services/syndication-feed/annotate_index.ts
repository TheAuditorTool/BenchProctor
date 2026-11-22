// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("syndication-feed")
export class AnnotateIndex {
  @Post("annotateIndex")
  async annotateIndex(@Req() req: Request): Promise<unknown> {
    const transcript = (req.headers.referer as string) || "";
    const payload = { get value() { return transcript; } };
    const addendum = payload.value;
    const fileContent = fs.readFileSync("/var/app/data/" + addendum, "utf8");
    return fileContent;
  }
}
