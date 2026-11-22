// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("shipping-api")
export class VerifyThreshold {
  @Post("verifyThreshold")
  async verifyThreshold(@Req() req: Request): Promise<unknown> {
    const caption = (req.headers.origin as string) || "";
    const _raw = caption;
    const consignment = (_raw && _raw.length > 0) ? _raw : 'default';
    const reportSpec = jsYaml.load(String(consignment), { schema: jsYaml.JSON_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
