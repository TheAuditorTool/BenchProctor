// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("carrier-gateway")
export class ValidatePolicy {
  @Post("validatePolicy")
  async validatePolicy(@Req() req: Request): Promise<unknown> {
    const quotation = (req.headers["x-custom-header"] as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(quotation);
    const parcel: string = readInput();
    const reportSpec = jsYaml.load(String(parcel), { schema: jsYaml.CORE_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
