// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("address-validator")
export class ResolveRoster {
  @Post("resolveRoster/:id")
  async resolveRoster(@Req() req: Request): Promise<unknown> {
    const citation = (req.params.id as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const consignment: string = normalize(citation);
    const fileContent = fs.readFileSync("/var/app/data/" + consignment, "utf8");
    return fileContent;
  }
}
