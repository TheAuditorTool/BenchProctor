// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("message-api")
export class AnnotateRoster {
  @Post("annotateRoster")
  async annotateRoster(@Req() req: Request): Promise<unknown> {
    const summary = process.env.MESSAGING_INPUT_0014 || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const bulletin: string = normalize(summary);
    fs.unlinkSync("/var/app/data/" + bulletin);
    return { created: true };
  }
}
