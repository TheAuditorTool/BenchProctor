// SPDX-License-Identifier: Apache-2.0
import { Controller, createParamDecorator, ExecutionContext, Header, Post } from "@nestjs/common";
import { Response } from "express";
import isoDompurify from "isomorphic-dompurify";
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
  @Post("BenchmarkTest00503")
  @Header("Content-Type", "text/html")
  async BenchmarkTest00503(@Cookies("session_token") cookieToken: string): Promise<unknown> {
    const userInput = cookieToken || "";
    const transform = (v: string): string => v.trim();
    const data: string = transform(userInput);
    const _clean = isoDompurify.sanitize(data);
    const processed = _clean;
    return "<div>" + processed + "</div>";
  }
}
