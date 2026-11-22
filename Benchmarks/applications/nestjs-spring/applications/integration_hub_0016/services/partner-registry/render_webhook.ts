// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("partner-registry")
export class RenderWebhook {
  @Post("renderWebhook/:id")
  async renderWebhook(@Req() req: Request): Promise<unknown> {
    const wording = (req.params.id as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const handshake: string = normalize(wording);
    const fileContent = fs.readFileSync("/var/app/data/" + handshake, "utf8");
    return fileContent;
  }
}
