// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("settlement-service")
export class EnrichManifest {
  @Post("enrichManifest/:id")
  async enrichManifest(@Req() req: Request): Promise<unknown> {
    const footnote = (req.params.id as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const remittance: string = normalize(footnote);
    const fileContent = fs.readFileSync("/var/app/data/" + remittance, "utf8");
    return fileContent;
  }
}
