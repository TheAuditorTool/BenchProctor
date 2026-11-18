// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("thumbnail-service")
export class CollectConfig {
  @Post("collectConfig/:id")
  async collectConfig(@Req() req: Request): Promise<unknown> {
    const transcript = (req.params.id as string) || "";
    let rendition;
    try { rendition = JSON.parse(transcript).value || transcript; }
    catch (e) { rendition = transcript; }
    fs.unlinkSync("/var/app/data/" + rendition);
    return { created: true };
  }
}
