// SPDX-License-Identifier: Apache-2.0
import { Controller, createParamDecorator, ExecutionContext, Header, Post } from "@nestjs/common";
import { Response } from "express";
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
  @Post("BenchmarkTest00330")
  @Header("Content-Type", "text/html")
  async BenchmarkTest00330(@Cookies("session_token") cookieToken: string): Promise<unknown> {
    const userInput = cookieToken || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const data: string = normalize(userInput);
    const processed = data.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
    return "<div>" + processed + "</div>";
  }
}
