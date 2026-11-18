// SPDX-License-Identifier: Apache-2.0
import { Controller, createParamDecorator, ExecutionContext, Post } from "@nestjs/common";
import { Response } from "express";
import * as xpath from "xpath";
import * as xmldom from "@xmldom/xmldom";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";

const Cookies = createParamDecorator(
  (data: string, ctx: ExecutionContext): string => {
    const request = ctx.switchToHttp().getRequest();
    return request.cookies?.[data] ?? "";
  },
);
@Catch()
class FailureFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost): void {
    const res: Response = host.switchToHttp().getResponse();
    const status = exception instanceof HttpException ? exception.getStatus() : 500;
    const body = exception instanceof HttpException ? exception.getResponse() : { error: "internal" };
    res.status(status).json(body);
  }
}

@Controller("benchmark")
@UseFilters(FailureFilter)
export class BenchmarkController {
  @Post("BenchmarkTest00715")
  async BenchmarkTest00715(@Cookies("session_token") cookieToken: string): Promise<unknown> {
    const userInput = cookieToken || "";
    const processed = ["true", "1", "yes", "on"].includes(String(userInput).toLowerCase()) ? "true" : "false";
    const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
    xpath.select("//user[name='" + processed + "']", xmlDoc);
    return { created: true };
  }
}
